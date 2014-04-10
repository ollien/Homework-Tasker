# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Homework.taskId'
        db.alter_column(u'HomeworkTasker_homework', 'taskId', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'Homework.taskId'
        db.alter_column(u'HomeworkTasker_homework', 'taskId', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'HomeworkTasker.homework': {
            'Meta': {'object_name': 'Homework'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['HomeworkTasker.Subject']"}),
            'taskId': ('django.db.models.fields.TextField', [], {}),
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