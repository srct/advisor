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

        # Adding M2M table for field coursestaken on 'Student'
        m2m_table_name = db.shorten_name(u'mainapp_student_coursestaken')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm[u'mainapp.student'], null=False)),
            ('course', models.ForeignKey(orm[u'mainapp.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['student_id', 'course_id'])

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
            ('number', self.gf('django.db.models.fields.IntegerField')()),
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

        # Adding M2M table for field programs on 'Semester'
        m2m_table_name = db.shorten_name(u'mainapp_semester_programs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('semester', models.ForeignKey(orm[u'mainapp.semester'], null=False)),
            ('program', models.ForeignKey(orm[u'mainapp.program'], null=False))
        ))
        db.create_unique(m2m_table_name, ['semester_id', 'program_id'])

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

        # Adding model 'Major'
        db.create_table(u'mainapp_major', (
            (u'program_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mainapp.Program'], unique=True, primary_key=True)),
            ('gened', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.GenEd'])),
            ('concentration', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.Concentration'], blank=True)),
        ))
        db.send_create_signal(u'mainapp', ['Major'])

        # Adding model 'Minor'
        db.create_table(u'mainapp_minor', (
            (u'program_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mainapp.Program'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'mainapp', ['Minor'])

        # Adding model 'GenEd'
        db.create_table(u'mainapp_gened', (
            (u'program_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mainapp.Program'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'mainapp', ['GenEd'])

        # Adding model 'Concentration'
        db.create_table(u'mainapp_concentration', (
            (u'program_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mainapp.Program'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'mainapp', ['Concentration'])

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
            ('dept', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('courseid', self.gf('django.db.models.fields.IntegerField')()),
            ('credits', self.gf('django.db.models.fields.IntegerField')()),
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

        # Removing M2M table for field coursestaken on 'Student'
        db.delete_table(db.shorten_name(u'mainapp_student_coursestaken'))

        # Deleting model 'AdvisorAdminUser'
        db.delete_table(u'mainapp_advisoradminuser')

        # Deleting model 'Semester'
        db.delete_table(u'mainapp_semester')

        # Removing M2M table for field courses on 'Semester'
        db.delete_table(db.shorten_name(u'mainapp_semester_courses'))

        # Removing M2M table for field programs on 'Semester'
        db.delete_table(db.shorten_name(u'mainapp_semester_programs'))

        # Deleting model 'Trajectory'
        db.delete_table(u'mainapp_trajectory')

        # Removing M2M table for field semesters on 'Trajectory'
        db.delete_table(db.shorten_name(u'mainapp_trajectory_semesters'))

        # Removing M2M table for field completed on 'Trajectory'
        db.delete_table(db.shorten_name(u'mainapp_trajectory_completed'))

        # Deleting model 'Program'
        db.delete_table(u'mainapp_program')

        # Removing M2M table for field courses on 'Program'
        db.delete_table(db.shorten_name(u'mainapp_program_courses'))

        # Deleting model 'Major'
        db.delete_table(u'mainapp_major')

        # Deleting model 'Minor'
        db.delete_table(u'mainapp_minor')

        # Deleting model 'GenEd'
        db.delete_table(u'mainapp_gened')

        # Deleting model 'Concentration'
        db.delete_table(u'mainapp_concentration')

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
            'programs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.Program']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Student']"})
        },
        u'mainapp.student': {
            'Meta': {'object_name': 'Student'},
            'advisorname': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mainapp.AdvisorAdminUser']", 'unique': 'True'}),
            'coursestaken': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.Course']", 'symmetrical': 'False'}),
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