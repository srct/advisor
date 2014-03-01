# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Program'
        db.create_table(u'mainapp_program', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name')),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'mainapp', ['Program'])

        # Adding M2M table for field courses on 'Program'
        m2m_table_name = db.shorten_name(u'mainapp_program_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('program', models.ForeignKey(orm[u'mainapp.program'], null=False)),
            ('metacourse', models.ForeignKey(orm[u'mainapp.metacourse'], null=False))
        ))
        db.create_unique(m2m_table_name, ['program_id', 'metacourse_id'])

        # Deleting field 'Minor.slug'
        db.delete_column(u'mainapp_minor', 'slug')

        # Deleting field 'Minor.description'
        db.delete_column(u'mainapp_minor', 'description')

        # Deleting field 'Minor.name'
        db.delete_column(u'mainapp_minor', 'name')

        # Deleting field 'Minor.created'
        db.delete_column(u'mainapp_minor', 'created')

        # Deleting field 'Minor.id'
        db.delete_column(u'mainapp_minor', u'id')

        # Deleting field 'Minor.modified'
        db.delete_column(u'mainapp_minor', 'modified')

        # Adding field 'Minor.program_ptr'
        db.add_column(u'mainapp_minor', u'program_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=None, to=orm['mainapp.Program'], unique=True, primary_key=True),
                      keep_default=False)

        # Removing M2M table for field courses on 'Minor'
        db.delete_table(db.shorten_name(u'mainapp_minor_courses'))

        # Deleting field 'GenEd.slug'
        db.delete_column(u'mainapp_gened', 'slug')

        # Deleting field 'GenEd.description'
        db.delete_column(u'mainapp_gened', 'description')

        # Deleting field 'GenEd.name'
        db.delete_column(u'mainapp_gened', 'name')

        # Deleting field 'GenEd.created'
        db.delete_column(u'mainapp_gened', 'created')

        # Deleting field 'GenEd.id'
        db.delete_column(u'mainapp_gened', u'id')

        # Deleting field 'GenEd.modified'
        db.delete_column(u'mainapp_gened', 'modified')

        # Adding field 'GenEd.program_ptr'
        db.add_column(u'mainapp_gened', u'program_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=None, to=orm['mainapp.Program'], unique=True, primary_key=True),
                      keep_default=False)

        # Removing M2M table for field courses on 'GenEd'
        db.delete_table(db.shorten_name(u'mainapp_gened_courses'))

        # Deleting field 'Major.slug'
        db.delete_column(u'mainapp_major', 'slug')

        # Deleting field 'Major.description'
        db.delete_column(u'mainapp_major', 'description')

        # Deleting field 'Major.name'
        db.delete_column(u'mainapp_major', 'name')

        # Deleting field 'Major.created'
        db.delete_column(u'mainapp_major', 'created')

        # Deleting field 'Major.id'
        db.delete_column(u'mainapp_major', u'id')

        # Deleting field 'Major.modified'
        db.delete_column(u'mainapp_major', 'modified')

        # Adding field 'Major.program_ptr'
        db.add_column(u'mainapp_major', u'program_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=None, to=orm['mainapp.Program'], unique=True, primary_key=True),
                      keep_default=False)

        # Removing M2M table for field courses on 'Major'
        db.delete_table(db.shorten_name(u'mainapp_major_courses'))

        # Deleting field 'Concentration.slug'
        db.delete_column(u'mainapp_concentration', 'slug')

        # Deleting field 'Concentration.description'
        db.delete_column(u'mainapp_concentration', 'description')

        # Deleting field 'Concentration.name'
        db.delete_column(u'mainapp_concentration', 'name')

        # Deleting field 'Concentration.created'
        db.delete_column(u'mainapp_concentration', 'created')

        # Deleting field 'Concentration.id'
        db.delete_column(u'mainapp_concentration', u'id')

        # Deleting field 'Concentration.modified'
        db.delete_column(u'mainapp_concentration', 'modified')

        # Adding field 'Concentration.program_ptr'
        db.add_column(u'mainapp_concentration', u'program_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=None, to=orm['mainapp.Program'], unique=True, primary_key=True),
                      keep_default=False)

        # Removing M2M table for field courses on 'Concentration'
        db.delete_table(db.shorten_name(u'mainapp_concentration_courses'))


    def backwards(self, orm):
        # Deleting model 'Program'
        db.delete_table(u'mainapp_program')

        # Removing M2M table for field courses on 'Program'
        db.delete_table(db.shorten_name(u'mainapp_program_courses'))

        # Adding field 'Minor.slug'
        db.add_column(u'mainapp_minor', 'slug',
                      self.gf('autoslug.fields.AutoSlugField')(default=None, max_length=50, unique_with=(), populate_from='name'),
                      keep_default=False)

        # Adding field 'Minor.description'
        db.add_column(u'mainapp_minor', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Minor.name'
        db.add_column(u'mainapp_minor', 'name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=50),
                      keep_default=False)

        # Adding field 'Minor.created'
        db.add_column(u'mainapp_minor', 'created',
                      self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Minor.id'
        db.add_column(u'mainapp_minor', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Adding field 'Minor.modified'
        db.add_column(u'mainapp_minor', 'modified',
                      self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now),
                      keep_default=False)

        # Deleting field 'Minor.program_ptr'
        db.delete_column(u'mainapp_minor', u'program_ptr_id')

        # Adding M2M table for field courses on 'Minor'
        m2m_table_name = db.shorten_name(u'mainapp_minor_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('minor', models.ForeignKey(orm[u'mainapp.minor'], null=False)),
            ('metacourse', models.ForeignKey(orm[u'mainapp.metacourse'], null=False))
        ))
        db.create_unique(m2m_table_name, ['minor_id', 'metacourse_id'])

        # Adding field 'GenEd.slug'
        db.add_column(u'mainapp_gened', 'slug',
                      self.gf('autoslug.fields.AutoSlugField')(default=None, max_length=50, unique_with=(), populate_from='name'),
                      keep_default=False)

        # Adding field 'GenEd.description'
        db.add_column(u'mainapp_gened', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'GenEd.name'
        db.add_column(u'mainapp_gened', 'name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=50),
                      keep_default=False)

        # Adding field 'GenEd.created'
        db.add_column(u'mainapp_gened', 'created',
                      self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'GenEd.id'
        db.add_column(u'mainapp_gened', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Adding field 'GenEd.modified'
        db.add_column(u'mainapp_gened', 'modified',
                      self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now),
                      keep_default=False)

        # Deleting field 'GenEd.program_ptr'
        db.delete_column(u'mainapp_gened', u'program_ptr_id')

        # Adding M2M table for field courses on 'GenEd'
        m2m_table_name = db.shorten_name(u'mainapp_gened_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gened', models.ForeignKey(orm[u'mainapp.gened'], null=False)),
            ('metacourse', models.ForeignKey(orm[u'mainapp.metacourse'], null=False))
        ))
        db.create_unique(m2m_table_name, ['gened_id', 'metacourse_id'])

        # Adding field 'Major.slug'
        db.add_column(u'mainapp_major', 'slug',
                      self.gf('autoslug.fields.AutoSlugField')(default=None, max_length=50, unique_with=(), populate_from='name'),
                      keep_default=False)

        # Adding field 'Major.description'
        db.add_column(u'mainapp_major', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Major.name'
        db.add_column(u'mainapp_major', 'name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=50),
                      keep_default=False)

        # Adding field 'Major.created'
        db.add_column(u'mainapp_major', 'created',
                      self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Major.id'
        db.add_column(u'mainapp_major', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Adding field 'Major.modified'
        db.add_column(u'mainapp_major', 'modified',
                      self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now),
                      keep_default=False)

        # Deleting field 'Major.program_ptr'
        db.delete_column(u'mainapp_major', u'program_ptr_id')

        # Adding M2M table for field courses on 'Major'
        m2m_table_name = db.shorten_name(u'mainapp_major_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('major', models.ForeignKey(orm[u'mainapp.major'], null=False)),
            ('metacourse', models.ForeignKey(orm[u'mainapp.metacourse'], null=False))
        ))
        db.create_unique(m2m_table_name, ['major_id', 'metacourse_id'])

        # Adding field 'Concentration.slug'
        db.add_column(u'mainapp_concentration', 'slug',
                      self.gf('autoslug.fields.AutoSlugField')(default=None, max_length=50, unique_with=(), populate_from='name'),
                      keep_default=False)

        # Adding field 'Concentration.description'
        db.add_column(u'mainapp_concentration', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Concentration.name'
        db.add_column(u'mainapp_concentration', 'name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=50),
                      keep_default=False)

        # Adding field 'Concentration.created'
        db.add_column(u'mainapp_concentration', 'created',
                      self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Concentration.id'
        db.add_column(u'mainapp_concentration', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Adding field 'Concentration.modified'
        db.add_column(u'mainapp_concentration', 'modified',
                      self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now),
                      keep_default=False)

        # Deleting field 'Concentration.program_ptr'
        db.delete_column(u'mainapp_concentration', u'program_ptr_id')

        # Adding M2M table for field courses on 'Concentration'
        m2m_table_name = db.shorten_name(u'mainapp_concentration_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('concentration', models.ForeignKey(orm[u'mainapp.concentration'], null=False)),
            ('metacourse', models.ForeignKey(orm[u'mainapp.metacourse'], null=False))
        ))
        db.create_unique(m2m_table_name, ['concentration_id', 'metacourse_id'])


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
        u'mainapp.concentration': {
            'Meta': {'object_name': 'Concentration', '_ormbases': [u'mainapp.Program']},
            u'program_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mainapp.Program']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'mainapp.course': {
            'Meta': {'object_name': 'Course', '_ormbases': [u'mainapp.MetaCourse']},
            'corequisites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'coreq+'", 'blank': 'True', 'to': u"orm['mainapp.MetaCourse']"}),
            'courseid': ('django.db.models.fields.IntegerField', [], {}),
            'credits': ('django.db.models.fields.IntegerField', [], {}),
            'dept': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'metacourse_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mainapp.MetaCourse']", 'unique': 'True', 'primary_key': 'True'}),
            'prerequisites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'prereq+'", 'blank': 'True', 'to': u"orm['mainapp.MetaCourse']"})
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
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"})
        },
        u'mainapp.minor': {
            'Meta': {'object_name': 'Minor', '_ormbases': [u'mainapp.Program']},
            u'program_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mainapp.Program']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'mainapp.program': {
            'Meta': {'object_name': 'Program'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.MetaCourse']", 'symmetrical': 'False'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"})
        },
        u'mainapp.semester': {
            'Meta': {'object_name': 'Semester'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.Course']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Student']"})
        },
        u'mainapp.student': {
            'Meta': {'object_name': 'Student'},
            'advisorname': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mainapp.AdvisorAdminUser']", 'unique': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'dateOfGrad': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Major']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'tj': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mainapp.Trajectory']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'mainapp.trajectory': {
            'Meta': {'object_name': 'Trajectory'},
            'completed': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.Course']", 'symmetrical': 'False'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'semesters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.Semester']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'tj'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['mainapp']