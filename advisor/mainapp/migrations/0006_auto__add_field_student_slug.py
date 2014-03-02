# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Student.slug'
        db.add_column(u'mainapp_student', 'slug',
                      self.gf('autoslug.fields.AutoSlugField')(max_length=50, unique_with=(), null=True, populate_from='name'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Student.slug'
        db.delete_column(u'mainapp_student', 'slug')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mainapp.advisoradminuser': {
            'Meta': {'object_name': 'AdvisorAdminUser'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'advisorname'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'mainapp.buildresponse': {
            'Meta': {'object_name': 'BuildResponse'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'programs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.Program']", 'symmetrical': 'False'}),
            'semester': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Semester']"})
        },
        u'mainapp.concentration': {
            'Meta': {'object_name': 'Concentration', '_ormbases': [u'mainapp.Program']},
            u'program_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mainapp.Program']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'mainapp.course': {
            'Meta': {'object_name': 'Course', '_ormbases': [u'mainapp.MetaCourse']},
            'corequisites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'coreq+'", 'blank': 'True', 'to': u"orm['mainapp.MetaCourse']"}),
            'courseid': ('django.db.models.fields.IntegerField', [], {}),
            'credits': ('django.db.models.fields.IntegerField', [], {}),
            'dept': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'metacourse_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mainapp.MetaCourse']", 'unique': 'True', 'primary_key': 'True'}),
            'prerequisites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'prereq+'", 'blank': 'True', 'to': u"orm['mainapp.MetaCourse']"}),
            'uniqname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'mainapp.coursegroup': {
            'Meta': {'object_name': 'CourseGroup', '_ormbases': [u'mainapp.MetaCourse']},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.Course']", 'symmetrical': 'False'}),
            u'metacourse_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mainapp.MetaCourse']", 'unique': 'True', 'primary_key': 'True'}),
            'numneeded': ('django.db.models.fields.IntegerField', [], {})
        },
        u'mainapp.gened': {
            'Meta': {'object_name': 'GenEd', '_ormbases': [u'mainapp.Program']},
            u'program_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mainapp.Program']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'mainapp.major': {
            'Meta': {'object_name': 'Major', '_ormbases': [u'mainapp.Program']},
            'concentration': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Concentration']", 'blank': 'True'}),
            'gened': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.GenEd']"}),
            u'program_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mainapp.Program']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'mainapp.metacourse': {
            'Meta': {'object_name': 'MetaCourse'},
            'catalogyear': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'title'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'mainapp.minor': {
            'Meta': {'object_name': 'Minor', '_ormbases': [u'mainapp.Program']},
            u'program_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mainapp.Program']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'mainapp.program': {
            'Meta': {'object_name': 'Program'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'requirements': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'reqs+'", 'symmetrical': 'False', 'to': u"orm['mainapp.Requirement']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"})
        },
        u'mainapp.requirement': {
            'Meta': {'object_name': 'Requirement'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.MetaCourse']", 'symmetrical': 'False'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'mainapp.semester': {
            'Meta': {'object_name': 'Semester'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.Course']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nextsemester': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Semester']", 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'programs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.Program']", 'symmetrical': 'False'}),
            'requirementssatisfied': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'reqssatisfied+'", 'blank': 'True', 'to': u"orm['mainapp.Requirement']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Student']"})
        },
        u'mainapp.student': {
            'Meta': {'object_name': 'Student'},
            'advisorname': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mainapp.AdvisorAdminUser']", 'unique': 'True', 'blank': 'True'}),
            'coursestaken': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.Course']", 'symmetrical': 'False', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'dateOfGrad': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'programs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.Program']", 'symmetrical': 'False'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'max_length': '50', 'unique_with': '()', 'null': 'True', 'populate_from': "'name'"}),
            'trajectory': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mainapp.Trajectory']", 'unique': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'mainapp.trajectory': {
            'Meta': {'object_name': 'Trajectory'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'semesters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.Semester']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'trajectory'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['mainapp']