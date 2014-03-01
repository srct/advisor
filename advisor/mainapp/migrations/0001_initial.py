# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table(u'mainapp_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('major', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.Major'])),
            ('tj', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mainapp.Trajectory'], unique=True)),
            ('dateOfGrad', self.gf('django.db.models.fields.DateField')()),
            ('advisorname', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mainapp.AdvisorAdminUser'], unique=True)),
        ))
        db.send_create_signal(u'mainapp', ['Student'])

        # Adding model 'AdvisorAdminUser'
        db.create_table(u'mainapp_advisoradminuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='advisorname', unique=True, to=orm['auth.User'])),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'mainapp', ['AdvisorAdminUser'])

        # Adding model 'Semester'
        db.create_table(u'mainapp_semester', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.Student'])),
        ))
        db.send_create_signal(u'mainapp', ['Semester'])

        # Adding M2M table for field courses on 'Semester'
        m2m_table_name = db.shorten_name(u'mainapp_semester_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('semester', models.ForeignKey(orm[u'mainapp.semester'], null=False)),
            ('course', models.ForeignKey(orm[u'mainapp.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['semester_id', 'course_id'])

        # Adding model 'Trajectory'
        db.create_table(u'mainapp_trajectory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='tj', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'mainapp', ['Trajectory'])

        # Adding M2M table for field semesters on 'Trajectory'
        m2m_table_name = db.shorten_name(u'mainapp_trajectory_semesters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trajectory', models.ForeignKey(orm[u'mainapp.trajectory'], null=False)),
            ('semester', models.ForeignKey(orm[u'mainapp.semester'], null=False))
        ))
        db.create_unique(m2m_table_name, ['trajectory_id', 'semester_id'])

        # Adding M2M table for field completed on 'Trajectory'
        m2m_table_name = db.shorten_name(u'mainapp_trajectory_completed')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trajectory', models.ForeignKey(orm[u'mainapp.trajectory'], null=False)),
            ('course', models.ForeignKey(orm[u'mainapp.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['trajectory_id', 'course_id'])

        # Adding model 'Major'
        db.create_table(u'mainapp_major', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name')),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gened', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.GenEd'])),
            ('concentration', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.Concentration'], blank=True)),
        ))
        db.send_create_signal(u'mainapp', ['Major'])

        # Adding M2M table for field courses on 'Major'
        m2m_table_name = db.shorten_name(u'mainapp_major_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('major', models.ForeignKey(orm[u'mainapp.major'], null=False)),
            ('metacourse', models.ForeignKey(orm[u'mainapp.metacourse'], null=False))
        ))
        db.create_unique(m2m_table_name, ['major_id', 'metacourse_id'])

        # Adding model 'Minor'
        db.create_table(u'mainapp_minor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name')),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'mainapp', ['Minor'])

        # Adding M2M table for field courses on 'Minor'
        m2m_table_name = db.shorten_name(u'mainapp_minor_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('minor', models.ForeignKey(orm[u'mainapp.minor'], null=False)),
            ('metacourse', models.ForeignKey(orm[u'mainapp.metacourse'], null=False))
        ))
        db.create_unique(m2m_table_name, ['minor_id', 'metacourse_id'])

        # Adding model 'GenEd'
        db.create_table(u'mainapp_gened', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name')),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'mainapp', ['GenEd'])

        # Adding M2M table for field courses on 'GenEd'
        m2m_table_name = db.shorten_name(u'mainapp_gened_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gened', models.ForeignKey(orm[u'mainapp.gened'], null=False)),
            ('metacourse', models.ForeignKey(orm[u'mainapp.metacourse'], null=False))
        ))
        db.create_unique(m2m_table_name, ['gened_id', 'metacourse_id'])

        # Adding model 'Concentration'
        db.create_table(u'mainapp_concentration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name')),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'mainapp', ['Concentration'])

        # Adding M2M table for field courses on 'Concentration'
        m2m_table_name = db.shorten_name(u'mainapp_concentration_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('concentration', models.ForeignKey(orm[u'mainapp.concentration'], null=False)),
            ('metacourse', models.ForeignKey(orm[u'mainapp.metacourse'], null=False))
        ))
        db.create_unique(m2m_table_name, ['concentration_id', 'metacourse_id'])

        # Adding model 'MetaCourse'
        db.create_table(u'mainapp_metacourse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name')),
            ('catalogyear', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'mainapp', ['MetaCourse'])

        # Adding model 'Course'
        db.create_table(u'mainapp_course', (
            (u'metacourse_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mainapp.MetaCourse'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'mainapp', ['Course'])

        # Adding M2M table for field prerequisites on 'Course'
        m2m_table_name = db.shorten_name(u'mainapp_course_prerequisites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm[u'mainapp.course'], null=False)),
            ('metacourse', models.ForeignKey(orm[u'mainapp.metacourse'], null=False))
        ))
        db.create_unique(m2m_table_name, ['course_id', 'metacourse_id'])

        # Adding M2M table for field corequisites on 'Course'
        m2m_table_name = db.shorten_name(u'mainapp_course_corequisites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm[u'mainapp.course'], null=False)),
            ('metacourse', models.ForeignKey(orm[u'mainapp.metacourse'], null=False))
        ))
        db.create_unique(m2m_table_name, ['course_id', 'metacourse_id'])

        # Adding model 'CourseGroup'
        db.create_table(u'mainapp_coursegroup', (
            (u'metacourse_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mainapp.MetaCourse'], unique=True, primary_key=True)),
            ('numneeded', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'mainapp', ['CourseGroup'])

        # Adding M2M table for field courses on 'CourseGroup'
        m2m_table_name = db.shorten_name(u'mainapp_coursegroup_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coursegroup', models.ForeignKey(orm[u'mainapp.coursegroup'], null=False)),
            ('course', models.ForeignKey(orm[u'mainapp.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coursegroup_id', 'course_id'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table(u'mainapp_student')

        # Deleting model 'AdvisorAdminUser'
        db.delete_table(u'mainapp_advisoradminuser')

        # Deleting model 'Semester'
        db.delete_table(u'mainapp_semester')

        # Removing M2M table for field courses on 'Semester'
        db.delete_table(db.shorten_name(u'mainapp_semester_courses'))

        # Deleting model 'Trajectory'
        db.delete_table(u'mainapp_trajectory')

        # Removing M2M table for field semesters on 'Trajectory'
        db.delete_table(db.shorten_name(u'mainapp_trajectory_semesters'))

        # Removing M2M table for field completed on 'Trajectory'
        db.delete_table(db.shorten_name(u'mainapp_trajectory_completed'))

        # Deleting model 'Major'
        db.delete_table(u'mainapp_major')

        # Removing M2M table for field courses on 'Major'
        db.delete_table(db.shorten_name(u'mainapp_major_courses'))

        # Deleting model 'Minor'
        db.delete_table(u'mainapp_minor')

        # Removing M2M table for field courses on 'Minor'
        db.delete_table(db.shorten_name(u'mainapp_minor_courses'))

        # Deleting model 'GenEd'
        db.delete_table(u'mainapp_gened')

        # Removing M2M table for field courses on 'GenEd'
        db.delete_table(db.shorten_name(u'mainapp_gened_courses'))

        # Deleting model 'Concentration'
        db.delete_table(u'mainapp_concentration')

        # Removing M2M table for field courses on 'Concentration'
        db.delete_table(db.shorten_name(u'mainapp_concentration_courses'))

        # Deleting model 'MetaCourse'
        db.delete_table(u'mainapp_metacourse')

        # Deleting model 'Course'
        db.delete_table(u'mainapp_course')

        # Removing M2M table for field prerequisites on 'Course'
        db.delete_table(db.shorten_name(u'mainapp_course_prerequisites'))

        # Removing M2M table for field corequisites on 'Course'
        db.delete_table(db.shorten_name(u'mainapp_course_corequisites'))

        # Deleting model 'CourseGroup'
        db.delete_table(u'mainapp_coursegroup')

        # Removing M2M table for field courses on 'CourseGroup'
        db.delete_table(db.shorten_name(u'mainapp_coursegroup_courses'))


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
            'Meta': {'object_name': 'Concentration'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.MetaCourse']", 'symmetrical': 'False'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"})
        },
        u'mainapp.course': {
            'Meta': {'object_name': 'Course', '_ormbases': [u'mainapp.MetaCourse']},
            'corequisites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'coreq+'", 'blank': 'True', 'to': u"orm['mainapp.MetaCourse']"}),
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
            'Meta': {'object_name': 'GenEd'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.MetaCourse']", 'symmetrical': 'False'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"})
        },
        u'mainapp.major': {
            'Meta': {'object_name': 'Major'},
            'concentration': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Concentration']", 'blank': 'True'}),
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.MetaCourse']", 'symmetrical': 'False'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gened': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.GenEd']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"})
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
            'Meta': {'object_name': 'Minor'},
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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