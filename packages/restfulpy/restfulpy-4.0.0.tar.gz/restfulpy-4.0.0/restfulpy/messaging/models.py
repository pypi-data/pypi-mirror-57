from nanohttp import settings
from sqlalchemy import Integer, ForeignKey, Unicode
from sqlalchemy.ext.declarative import declared_attr

from ..orm import Field, FakeJSON,synonym
from ..taskqueue import RestfulpyTask
from .providers import create_messenger


class Email(RestfulpyTask):
    __tablename__ = 'email'


    template_filename = Field(Unicode(200), nullable=True)
    to = Field(Unicode(254), json='to')
    subject = Field(Unicode(254), json='subject')
    cc = Field(Unicode(254), nullable=True, json='cc')
    bcc = Field(Unicode(254), nullable=True, json='bcc')
    _body = Field('body', FakeJSON)

    from_ = Field(
        Unicode(254),
        json='from',
        default=lambda: settings.messaging.default_sender
    )

    __mapper_args__ = {
        'polymorphic_identity': __tablename__
    }

    def _set_body(self, body):
        self._body = body

    def _get_body(self):
        return self._body

    @declared_attr
    def body(cls):
        return synonym(
            '_body',
            descriptor=property(cls._get_body, cls._set_body)
        )

    @declared_attr
    def id(cls):
        return Field(
            Integer,
            ForeignKey('restfulpy_task.id'),
            primary_key=True, json='id'
        )

    def do_(self, context, attachments=None):
        messenger = create_messenger()
        messenger.send(
            self.to,
            self.subject,
            self.body,
            cc=self.cc,
            bcc=self.bcc,
            template_filename=self.template_filename,
            from_=self.from_,
            attachments=attachments
        )

        print('%s is sent to %s', self.subject, self.to)

