# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TransGallery'
        db.create_table(u'main_transgallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('lang', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('translation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translation', to=orm['galleries.Gallery'])),
        ))
        db.send_create_signal(u'main', ['TransGallery'])

        # Adding model 'TransGalleryImage'
        db.create_table(u'main_transgalleryimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('lang', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('translation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translation', to=orm['galleries.GalleryImage'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
        ))
        db.send_create_signal(u'main', ['TransGalleryImage'])

        # Adding model 'TransForm'
        db.create_table(u'main_transform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('lang', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('translation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translation', to=orm['forms.Form'])),
            ('button_text', self.gf('django.db.models.fields.CharField')(default=u'Submit', max_length=50)),
            ('response', self.gf('mezzanine.core.fields.RichTextField')()),
        ))
        db.send_create_signal(u'main', ['TransForm'])

        # Adding unique constraint on 'TransForm', fields ['lang', 'translation']
        db.create_unique(u'main_transform', ['lang', 'translation_id'])

        # Adding model 'TransLinkPage'
        db.create_table(u'main_translinkpage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('lang', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('translation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translation', to=orm['pages.Link'])),
        ))
        db.send_create_signal(u'main', ['TransLinkPage'])

        # Adding unique constraint on 'TransLinkPage', fields ['lang', 'translation']
        db.create_unique(u'main_translinkpage', ['lang', 'translation_id'])

        # Adding model 'TransRichTextPage'
        db.create_table(u'main_transrichtextpage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('lang', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('translation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translation', to=orm['pages.RichTextPage'])),
        ))
        db.send_create_signal(u'main', ['TransRichTextPage'])

        # Adding unique constraint on 'TransRichTextPage', fields ['lang', 'translation']
        db.create_unique(u'main_transrichtextpage', ['lang', 'translation_id'])

        # Adding model 'TransField'
        db.create_table(u'main_transfield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lang', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('translation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translation', to=orm['forms.Field'])),
            ('original', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('choices', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'main', ['TransField'])


    def backwards(self, orm):
        # Removing unique constraint on 'TransRichTextPage', fields ['lang', 'translation']
        db.delete_unique(u'main_transrichtextpage', ['lang', 'translation_id'])

        # Removing unique constraint on 'TransLinkPage', fields ['lang', 'translation']
        db.delete_unique(u'main_translinkpage', ['lang', 'translation_id'])

        # Removing unique constraint on 'TransForm', fields ['lang', 'translation']
        db.delete_unique(u'main_transform', ['lang', 'translation_id'])

        # Deleting model 'TransGallery'
        db.delete_table(u'main_transgallery')

        # Deleting model 'TransGalleryImage'
        db.delete_table(u'main_transgalleryimage')

        # Deleting model 'TransForm'
        db.delete_table(u'main_transform')

        # Deleting model 'TransLinkPage'
        db.delete_table(u'main_translinkpage')

        # Deleting model 'TransRichTextPage'
        db.delete_table(u'main_transrichtextpage')

        # Deleting model 'TransField'
        db.delete_table(u'main_transfield')


    models = {
        u'forms.field': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Field'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'choices': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.IntegerField', [], {}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'fields'", 'to': u"orm['forms.Form']"}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'placeholder_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'forms.form': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Form', '_ormbases': [u'pages.Page']},
            'button_text': ('django.db.models.fields.CharField', [], {'default': "u'Submit'", 'max_length': '50'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'email_copies': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email_from': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'email_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email_subject': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'response': ('mezzanine.core.fields.RichTextField', [], {}),
            'send_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'galleries.gallery': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Gallery', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'zip_import': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'galleries.galleryimage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'GalleryImage'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'file': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'images'", 'to': u"orm['galleries.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.homepage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'HomePage', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'content_heading': ('django.db.models.fields.CharField', [], {'default': "'About us!'", 'max_length': '200'}),
            'featured_portfolio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Portfolio']", 'null': 'True', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'main.order': {
            'Meta': {'object_name': 'Order'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'date_time': ('django.db.models.fields.DateField', [], {'max_length': '50'}),
            'frequency_of_service': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type_of_service': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'main.portfolio': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Portfolio', '_ormbases': [u'pages.Page']},
            'columns': ('django.db.models.fields.CharField', [], {'default': "'3'", 'max_length': '1'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'main.portfolioitem': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'PortfolioItem', '_ormbases': [u'pages.Page']},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'portfolioitems'", 'blank': 'True', 'to': u"orm['main.PortfolioItemCategory']"}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'featured_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'href': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'short_description': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'})
        },
        u'main.portfolioitemcategory': {
            'Meta': {'ordering': "('title',)", 'object_name': 'PortfolioItemCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'main.portfolioitemimage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'PortfolioItemImage'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'file': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portfolioitem': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['main.PortfolioItem']"})
        },
        u'main.slide': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Slide'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'to': u"orm['main.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_back': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'image_front': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'})
        },
        u'main.tablecell': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'TableCell', '_ormbases': [u'pages.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'row1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'row2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'row3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'row4': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'row5': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'row6': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'row7': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'main.transfield': {
            'Meta': {'ordering': "('lang',)", 'object_name': 'TransField'},
            'choices': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'original': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'translation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translation'", 'to': u"orm['forms.Field']"})
        },
        u'main.transform': {
            'Meta': {'ordering': "('lang',)", 'unique_together': "(('lang', 'translation'),)", 'object_name': 'TransForm'},
            'button_text': ('django.db.models.fields.CharField', [], {'default': "u'Submit'", 'max_length': '50'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'response': ('mezzanine.core.fields.RichTextField', [], {}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'translation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translation'", 'to': u"orm['forms.Form']"})
        },
        u'main.transgallery': {
            'Meta': {'ordering': "('lang',)", 'object_name': 'TransGallery'},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'translation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translation'", 'to': u"orm['galleries.Gallery']"})
        },
        u'main.transgalleryimage': {
            'Meta': {'ordering': "('lang',)", 'object_name': 'TransGalleryImage'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'translation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translation'", 'to': u"orm['galleries.GalleryImage']"})
        },
        u'main.translinkpage': {
            'Meta': {'ordering': "('lang',)", 'unique_together': "(('lang', 'translation'),)", 'object_name': 'TransLinkPage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'translation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translation'", 'to': u"orm['pages.Link']"})
        },
        u'main.transrichtextpage': {
            'Meta': {'ordering': "('lang',)", 'unique_together': "(('lang', 'translation'),)", 'object_name': 'TransRichTextPage'},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'translation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translation'", 'to': u"orm['pages.RichTextPage']"})
        },
        u'pages.link': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Link', '_ormbases': [u'pages.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'pages.richtextpage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'RichTextPage', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['main']