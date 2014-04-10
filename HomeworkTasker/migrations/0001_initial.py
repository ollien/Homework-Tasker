# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'HomeworkTasker_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.TextField')()),
            ('password', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.TextField')()),
            ('salt', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'HomeworkTasker', ['User'])

        # Adding model 'Session'
        db.create_table(u'HomeworkTasker_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sessionId', self.gf('django.db.models.fields.TextField')()),
            ('userId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['HomeworkTasker.User'])),
            ('persist', self.gf('django.db.models.fields.BooleanField')()),
            ('accessed', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'HomeworkTasker', ['Session'])

        # Adding model 'Subject'
        db.create_table(u'HomeworkTasker_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['HomeworkTasker.User'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'HomeworkTasker', ['Subject'])

        # Adding model 'Homework'
        db.create_table(u'HomeworkTasker_homework', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['HomeworkTasker.User'])),
            ('label', self.gf('django.db.models.fields.TextField')()),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['HomeworkTasker.Subject'])),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'HomeworkTasker', ['Homework'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'HomeworkTasker_user')

        # Deleting model 'Session'
        db.delete_table(u'HomeworkTasker_session')

        # Deleting model 'Subject'
        db.delete_table(u'HomeworkTasker_subject')

        # Deleting model 'Homework'
        db.delete_table(u'HomeworkTasker_homework')


    models = {
        u'HomeworkTasker.homework': {
            'Meta': {'object_name': 'Homework'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['HomeworkTasker.Subject']"}),
            'userId': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['HomeworkTasker.User']"})
        },
        u'HomeworkTasker.session': {
            'Meta': {'object_name': 'Session'},
            'accessed': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persist': ('django.db.models.fields.BooleanField', [], {}),
            'sessionId': ('django.db.models.fields.TextField', [], {}),
            'userId': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['HomeworkTasker.User']"})
        },
        u'HomeworkTasker.subject': {
            'Meta': {'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'userId': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['HomeworkTasker.User']"})
        },
        u'HomeworkTasker.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.TextField', [], {}),
            'salt': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['HomeworkTasker']