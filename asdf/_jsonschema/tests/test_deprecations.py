from unittest import TestCase
import importlib
import subprocess
import sys

from asdf._jsonschema import FormatChecker, validators


class TestDeprecations(TestCase):
    def test_validators_ErrorTree(self):
        """
        As of v4.0.0, importing ErrorTree from asdf._jsonschema.validators is
        deprecated in favor of doing so from asdf._jsonschema.exceptions.
        """

        with self.assertWarns(DeprecationWarning) as w:
            from asdf._jsonschema.validators import ErrorTree  # noqa

        self.assertEqual(w.filename, __file__)
        self.assertTrue(
            str(w.warning).startswith(
                "Importing ErrorTree from asdf._jsonschema.validators is deprecated",
            ),
        )

    def test_validators_validators(self):
        """
        As of v4.0.0, accessing asdf._jsonschema.validators.validators is
        deprecated.
        """

        with self.assertWarns(DeprecationWarning) as w:
            value = validators.validators
        self.assertEqual(value, validators._VALIDATORS)

        self.assertEqual(w.filename, __file__)
        self.assertTrue(
            str(w.warning).startswith(
                "Accessing asdf._jsonschema.validators.validators is deprecated",
            ),
        )

    def test_validators_meta_schemas(self):
        """
        As of v4.0.0, accessing asdf._jsonschema.validators.meta_schemas is
        deprecated.
        """

        with self.assertWarns(DeprecationWarning) as w:
            value = validators.meta_schemas
        self.assertEqual(value, validators._META_SCHEMAS)

        self.assertEqual(w.filename, __file__)
        self.assertTrue(
            str(w.warning).startswith(
                "Accessing asdf._jsonschema.validators.meta_schemas is deprecated",
            ),
        )

    def test_RefResolver_in_scope(self):
        """
        As of v4.0.0, RefResolver.in_scope is deprecated.
        """

        resolver = validators.RefResolver.from_schema({})
        with self.assertWarns(DeprecationWarning) as w:
            with resolver.in_scope("foo"):
                pass

        self.assertEqual(w.filename, __file__)
        self.assertTrue(
            str(w.warning).startswith(
                "asdf._jsonschema.RefResolver.in_scope is deprecated ",
            ),
        )

    def test_Validator_is_valid_two_arguments(self):
        """
        As of v4.0.0, calling is_valid with two arguments (to provide a
        different schema) is deprecated.
        """

        validator = validators.Draft4Validator({})
        with self.assertWarns(DeprecationWarning) as w:
            result = validator.is_valid("foo", {"type": "number"})

        self.assertFalse(result)
        self.assertEqual(w.filename, __file__)
        self.assertTrue(
            str(w.warning).startswith(
                "Passing a schema to Validator.is_valid is deprecated ",
            ),
        )

    def test_Validator_iter_errors_two_arguments(self):
        """
        As of v4.0.0, calling iter_errors with two arguments (to provide a
        different schema) is deprecated.
        """

        validator = validators.Draft4Validator({})
        with self.assertWarns(DeprecationWarning) as w:
            error, = validator.iter_errors("foo", {"type": "number"})

        self.assertEqual(error.validator, "type")
        self.assertEqual(w.filename, __file__)
        self.assertTrue(
            str(w.warning).startswith(
                "Passing a schema to Validator.iter_errors is deprecated ",
            ),
        )

    def test_Validator_subclassing(self):
        """
        As of v4.12.0, subclassing a validator class produces an explicit
        deprecation warning.

        This was never intended to be public API (and some comments over the
        years in issues said so, but obviously that's not a great way to make
        sure it's followed).

        A future version will explicitly raise an error.
        """

        with self.assertWarns(DeprecationWarning) as w:
            class Subclass(validators.Draft4Validator):
                pass

        self.assertEqual(w.filename, __file__)
        self.assertTrue(
            str(w.warning).startswith("Subclassing validator classes is "),
        )

        with self.assertWarns(DeprecationWarning) as w:
            class AnotherSubclass(validators.create(meta_schema={})):
                pass

    def test_FormatChecker_cls_checks(self):
        """
        As of v4.14.0, FormatChecker.cls_checks is deprecated without
        replacement.
        """

        self.addCleanup(FormatChecker.checkers.pop, "boom", None)

        with self.assertWarns(DeprecationWarning) as w:
            FormatChecker.cls_checks("boom")

        self.assertEqual(w.filename, __file__)
        self.assertTrue(
            str(w.warning).startswith("FormatChecker.cls_checks "),
        )
