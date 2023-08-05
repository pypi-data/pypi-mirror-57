# -*- coding: utf-8 -*-

import typing as ty
import collections
import weakref
import inspect

import click
from click.core import augment_usage_errors

from ._helpers import (
    get_callback_and_params,
    get_fake_option_name,
    raise_mixing_decorators_error,
)


class GroupedOption(click.Option):
    """Represents grouped (related) optional values
    """

    def __init__(self, param_decls=None, *, group: 'OptionGroup', **attrs):
        for attr in group.forbidden_option_attrs:
            if attr in attrs:
                raise TypeError(
                    f"'{attr}' attribute is not allowed for '{type(group).__name__}' options.")

        self.__group = group
        super().__init__(param_decls, **attrs)

    @property
    def group(self) -> 'OptionGroup':
        """Returns the group for this option

        :return: [OptionGroup] the group for this option
        """
        return self.__group

    def handle_parse_result(self, ctx, opts, args):
        with augment_usage_errors(ctx, param=self):
            self.group.handle_parse_result(self, ctx, opts)
        return super().handle_parse_result(ctx, opts, args)

    def get_help_record(self, ctx: click.Context):
        opts, opt_help = super().get_help_record(ctx)

        formatter = ctx.make_formatter()
        with formatter.indentation():
            indent = ' ' * formatter.current_indent
            return f'{indent}{opts}', opt_help


class _GroupTitleFakeOption(click.Option):
    """The helper `Option` class to display option group title in --help
    """

    def __init__(self, param_decls=None, *, group: 'OptionGroup', **attrs):
        self.__group = group
        super().__init__(param_decls, expose_value=False, **attrs)

    def get_help_record(self, ctx: click.Context):
        return self.__group.get_help_record(ctx)


class OptionGroup:
    """Option group manages grouped (related) options
    """

    def __init__(self, name: ty.Optional[str] = None, *,
                 help: ty.Optional[str] = None) -> None:
        self._name = name if name else ''
        self._help = inspect.cleandoc(help if help else '')

        self._options = collections.defaultdict(weakref.WeakValueDictionary)
        self._group_title_options = weakref.WeakValueDictionary()

    @property
    def name(self) -> str:
        """Returns the group name or empty string if it was not set

        :return: group name
        """
        return self._name

    @property
    def help(self) -> str:
        """Returns the group help or empty string if it was not set

        :return: group help
        """
        return self._help

    @property
    def name_extra(self) -> ty.List[str]:
        return []

    @property
    def forbidden_option_attrs(self) -> ty.List[str]:
        return []

    def get_default_name(self, ctx: click.Context) -> str:
        """Returns default name for the group

        :param ctx: Click Context object
        :return: group default name
        """
        if self.name:
            return self.name

        option_names = '|'.join(self.get_option_names(ctx))
        return f'({option_names})'

    def get_help_record(self, ctx: click.Context) -> ty.Tuple[str, str]:
        """Returns the help record for the group

        :param ctx: Click Context object
        :return: the tuple of two fileds: (name, help)
        """

        name = self.get_default_name(ctx)
        help_ = self.help if self.help else ''

        extra = ', '.join(self.name_extra)
        if extra:
            extra = f'[{extra}]'

        name = f'{name}: {extra}'

        return name, help_

    def option(self, *param_decls, **attrs):
        """Decorator attaches an grouped option to the command
        """

        def decorator(func):
            option_attrs = attrs.copy()
            option_attrs.setdefault('cls', GroupedOption)

            if not issubclass(option_attrs['cls'], GroupedOption):
                raise TypeError("'cls' argument must be a subclass of 'GroupedOption' class.")

            self._check_mixing_decorators(func)
            func = click.option(*param_decls, group=self, **option_attrs)(func)
            self._option_memo(func)

            # Add the fake invisible option to use for print nice title help for grouped options
            self._add_title_fake_option(func)

            return func

        return decorator

    def get_options(self, ctx: click.Context) -> ty.Dict[str, GroupedOption]:
        return self._options.get(ctx.command.callback, {})

    def get_option_names(self, ctx: click.Context) -> ty.List[str]:
        return list(reversed(list(self.get_options(ctx))))

    def get_error_hint(self, ctx, option_names: ty.Optional[ty.Set[str]] = None) -> str:
        options = self.get_options(ctx)
        text = ''

        for name, opt in reversed(list(options.items())):
            if option_names and name not in option_names:
                continue
            text += f'  {opt.get_error_hint(ctx)}\n'

        if text:
            text = text[:-1]

        return text

    def handle_parse_result(self, option: GroupedOption, ctx: click.Context, opts: dict) -> None:
        pass

    def _check_mixing_decorators(self, func):
        func, params = get_callback_and_params(func)

        if not params or func not in self._options:
            return

        last_param = params[-1]
        title_option = self._group_title_options[func]
        options = self._options[func]

        if last_param.name != title_option.name and last_param.name not in options:
            raise_mixing_decorators_error(last_param, func)

    def _add_title_fake_option(self, func):
        callback, params = get_callback_and_params(func)

        if callback not in self._group_title_options:
            func = click.option(get_fake_option_name(),
                                group=self, cls=_GroupTitleFakeOption)(func)

            _, params = get_callback_and_params(func)
            self._group_title_options[callback] = params[-1]

        title_option = self._group_title_options[callback]
        last_option = params[-1]

        if title_option.name != last_option.name:
            # Hold title fake option on the top of the option group
            title_index = params.index(title_option)
            params[-1], params[title_index] = params[title_index], params[-1]

    def _option_memo(self, func):
        func, params = get_callback_and_params(func)
        option = params[-1]
        self._options[func][option.name] = option


class RequiredAnyOptionGroup(OptionGroup):
    """Option group with required any options of this group
    """

    @property
    def forbidden_option_attrs(self) -> ty.List[str]:
        return ['required']

    @property
    def name_extra(self) -> ty.List[str]:
        return super().name_extra + ['required_any']

    def handle_parse_result(self, option: GroupedOption, ctx: click.Context, opts: dict) -> None:
        if option.name in opts:
            return

        option_names = set(self.get_options(ctx))

        if not option_names.intersection(opts):
            error_text = f'Missing one of the required options from "{self.get_default_name(ctx)}" option group:'
            error_text += f'\n{self.get_error_hint(ctx)}'

            raise click.UsageError(error_text, ctx=ctx)


class RequiredAllOptionGroup(OptionGroup):
    """Option group with required all options of this group
    """

    @property
    def forbidden_option_attrs(self) -> ty.List[str]:
        return ['required']

    @property
    def name_extra(self) -> ty.List[str]:
        return super().name_extra + ['required_all']

    def handle_parse_result(self, option: GroupedOption, ctx: click.Context, opts: dict) -> None:
        option_names = set(self.get_options(ctx))

        if not option_names.issubset(opts):
            required_names = option_names.difference(option_names.intersection(opts))

            error_text = f'Missing all required options from "{self.get_default_name(ctx)}" option group:'
            error_text += f'\n{self.get_error_hint(ctx, required_names)}'

            raise click.UsageError(error_text, ctx=ctx)


class MutuallyExclusiveOptionGroup(OptionGroup):
    """Option group with mutually exclusive behavior for grouped options
    """

    def __init__(self, name: ty.Optional[str] = None, *,
                 help: ty.Optional[str] = None,
                 required: bool = False) -> None:
        super().__init__(name, help=help)
        self._required = required

    @property
    def required(self) -> bool:
        """Returns 'required' flag

        If 'required' is True, at least one option from the group must be set.

        :return: required flag
        """
        return self._required

    @property
    def forbidden_option_attrs(self) -> ty.List[str]:
        return ['required']

    @property
    def name_extra(self) -> ty.List[str]:
        required = ['required'] if self.required else []
        return super().name_extra + ['mutually_exclusive'] + required

    def handle_parse_result(self, option: GroupedOption, ctx: click.Context, opts: dict) -> None:
        option_names = set(self.get_options(ctx))
        given_option_names = option_names.intersection(opts)
        given_option_count = len(given_option_names)

        if given_option_count > 1:
            error_text = f'The given mutually exclusive options cannot be used at the same time:'
            error_text += f'\n{self.get_error_hint(ctx, given_option_names)}'
            raise click.UsageError(error_text, ctx=ctx)

        elif self.required and given_option_count == 0:
            error_text = ('Missing one of the required mutually exclusive options from '
                          f'"{self.get_default_name(ctx)}" option group:')
            error_text += f'\n{self.get_error_hint(ctx)}'
            raise click.UsageError(error_text, ctx=ctx)
