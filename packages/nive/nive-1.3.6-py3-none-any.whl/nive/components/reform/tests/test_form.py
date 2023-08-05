import unittest

class TestForm(unittest.TestCase):
    def _makeOne(self, schema, **kw):
        from nive.components.reform.form import Form
        return Form(schema, **kw)

    def test_ctor_buttons_strings(self):
        from nive.components.reform.widget import FormWidget
        schema = DummySchema()
        form = self._makeOne(schema, renderer='abc', action='action',
                             method='method', buttons=('button',),
                             formid='formid')
        self.assertEqual(form.schema, schema)
        self.assertEqual(form.renderer, 'abc')
        self.assertEqual(form.action, 'action')
        self.assertEqual(form.method, 'method')
        self.assertEqual(form.formid, 'formid')
        self.assertEqual(form.widget.__class__, FormWidget)
        self.assertEqual(len(form.buttons), 1)
        button = form.buttons[0]
        self.assertEqual(button.name, 'button')
        self.assertEqual(button.value, 'button')
        self.assertEqual(button.title, 'Button')

    def test_ctor_buttons_notstrings(self):
        from nive.components.reform.widget import FormWidget
        schema = DummySchema()
        form = self._makeOne(schema, renderer='abc', action='action',
                             method='method', buttons=(None,), formid='formid')
        self.assertEqual(form.schema, schema)
        self.assertEqual(form.renderer, 'abc')
        self.assertEqual(form.action, 'action')
        self.assertEqual(form.method, 'method')
        self.assertEqual(form.formid, 'formid')
        self.assertEqual(form.widget.__class__, FormWidget)
        self.assertEqual(len(form.buttons), 1)
        button = form.buttons[0]
        self.assertEqual(button, None)

    def test_ctor_passes_unknown_kwargs(self):
        schema = DummySchema()
        schema.children = [DummySchema()]
        form = self._makeOne(schema, a='a', b='b')
        self.assertEqual(form.schema, schema)
        self.assertEqual(form.a, 'a')
        self.assertEqual(form.b, 'b')
        child = form.children[0]
        self.assertEqual(child.a, 'a')
        self.assertEqual(child.b, 'b')


class TestIssues(unittest.TestCase):

    def test_issue_54(self):
        from nive.components import reform
        class LoginForm(reform.schema.Schema):
            username = reform.schema.SchemaNode(reform.schema.String())
            password = reform.schema.SchemaNode(reform.schema.String(),
                                           widget=reform.widget.PasswordWidget())
        def validate_password(node, d):
            raise reform.schema.Invalid(node,
                                   'Username does not match password')
        loginform = LoginForm(validator=validate_password)
        data = [('username', 'kai'),
                ('password', '123')]
        try:
            reform.Form(loginform).validate(data)
        except reform.ValidationFailure as e:
            rendered = e.render()
            self.assertTrue(
                'Username does not match password' in rendered
            )

class TestButton(unittest.TestCase):
    def _makeOne(self, **kw):
        from nive.components.reform.form import Button
        return Button(**kw)

    def test_ctor_title_None(self):
        button = self._makeOne()
        self.assertEqual(button.title, 'Submit')

    def test_ctor_type_None(self):
        button = self._makeOne()
        self.assertEqual(button.type, 'submit')

    def test_ctor_value_None(self):
        button = self._makeOne()
        self.assertEqual(button.value, 'submit')

    def test_name_with_space(self):
        button = self._makeOne(name="log\tin as a user")
        self.assertEqual(button.name, 'log_in_as_a_user')
        self.assertEqual(button.value, 'log_in_as_a_user')

    def test_ctor(self):
        button = self._makeOne(name='name', title='title',
                               type='type', value='value', disabled=True)
        self.assertEqual(button.value, 'value')
        self.assertEqual(button.name, 'name')
        self.assertEqual(button.title, 'title')
        self.assertEqual(button.type, 'type')
        self.assertEqual(button.disabled, True)

class TestRaw(unittest.TestCase):
    def _makeOne(self, val):
        from nive.components.reform.form import Raw
        return Raw(val)

    def test___html__(self):
        inst = self._makeOne('abc')
        self.assertEqual(inst.__html__(), 'abc')

class DummySchema(object):
    typ = None
    name = 'name'
    title = 'title'
    description = 'description'
    required = True
    children = ()
    default = 'default'
    sdefault = 'sdefault'
    def __init__(self, exc=None):
        self.exc = exc
