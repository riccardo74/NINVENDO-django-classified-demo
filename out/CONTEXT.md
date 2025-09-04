# Project Snapshot

_Generated on 2025-09-03 23:31:27_


---

## Project Tree (filtered)

```
NINVENDO-django-classified-demo/
├── demo/
│   ├── craigslist_data/
│   │   ├── Areas.json
│   │   ├── Categories.json
│   │   └── Types.json
│   ├── management/
│   │   └── commands/
│   │       └── setup_project.py
│   ├── templates/
│   │   └── demo/
│   │       └── login.html
│   ├── __init__.py
│   └── tests.py
├── logs/
├── out/
│   ├── CONTEXT.md
│   └── GIT_HISTORY.txt
├── payments/
│   ├── templatetags/
│   │   ├── __init__.py
│   │   └── payments_tag.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processor.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── urls.py
│   └── views.py
├── project/
│   ├── management/
│   │   ├── commands/
│   │   │   ├── __init__.py
│   │   │   └── cloudinary_admin.py
│   │   └── __init__.py
│   ├── templatetags/
│   │   ├── __init__.py
│   │   ├── cloudinary_tags.py
│   │   └── site_tags.py
│   ├── __init__.py
│   ├── apps.py
│   ├── cloudinary_signals.py
│   ├── cloudinary_utils.py
│   ├── context_processors.py
│   ├── settings.py
│   └── urls.py
├── static/
│   ├── admin/
│   │   ├── css/
│   │   │   ├── vendor/
│   │   │   │   └── select2/
│   │   │   │       ├── LICENSE-SELECT2.f94142512c91.md
│   │   │   │       ├── LICENSE-SELECT2.f94142512c91.md.gz
│   │   │   │       ├── LICENSE-SELECT2.md
│   │   │   │       ├── LICENSE-SELECT2.md.gz
│   │   │   │       ├── select2.a2194c262648.css
│   │   │   │       ├── select2.a2194c262648.css.gz
│   │   │   │       ├── select2.css
│   │   │   │       ├── select2.css.gz
│   │   │   │       ├── select2.min.9f54e6414f87.css
│   │   │   │       ├── select2.min.9f54e6414f87.css.gz
│   │   │   │       ├── select2.min.css
│   │   │   │       └── select2.min.css.gz
│   │   │   ├── autocomplete.css
│   │   │   ├── autocomplete.css.gz
│   │   │   ├── autocomplete.d24f10bdee41.css
│   │   │   ├── autocomplete.d24f10bdee41.css.gz
│   │   │   ├── base.08e8df8c3104.css
│   │   │   ├── base.08e8df8c3104.css.gz
│   │   │   ├── base.css
│   │   │   ├── base.css.gz
│   │   │   ├── changelists.59465e72d1ef.css
│   │   │   ├── changelists.59465e72d1ef.css.gz
│   │   │   ├── changelists.css
│   │   │   ├── changelists.css.gz
│   │   │   ├── dark_mode.css
│   │   │   ├── dark_mode.css.gz
│   │   │   ├── dark_mode.f9ffd47267af.css
│   │   │   ├── dark_mode.f9ffd47267af.css.gz
│   │   │   ├── dashboard.css
│   │   │   ├── dashboard.css.gz
│   │   │   ├── dashboard.e90f2068217b.css
│   │   │   ├── dashboard.e90f2068217b.css.gz
│   │   │   ├── forms.86203f0362cc.css
│   │   │   ├── forms.86203f0362cc.css.gz
│   │   │   ├── forms.css
│   │   │   ├── forms.css.gz
│   │   │   ├── login.a3b47c458e5d.css
│   │   │   ├── login.a3b47c458e5d.css.gz
│   │   │   ├── login.css
│   │   │   ├── login.css.gz
│   │   │   ├── nav_sidebar.css
│   │   │   ├── nav_sidebar.css.gz
│   │   │   ├── nav_sidebar.dd925738f4cc.css
│   │   │   ├── nav_sidebar.dd925738f4cc.css.gz
│   │   │   ├── responsive.ae7b57af01c8.css
│   │   │   ├── responsive.ae7b57af01c8.css.gz
│   │   │   ├── responsive.css
│   │   │   ├── responsive.css.gz
│   │   │   ├── responsive_rtl.a154194876ee.css
│   │   │   ├── responsive_rtl.a154194876ee.css.gz
│   │   │   ├── responsive_rtl.css
│   │   │   ├── responsive_rtl.css.gz
│   │   │   ├── rtl.7e532512b807.css
│   │   │   ├── rtl.7e532512b807.css.gz
│   │   │   ├── rtl.css
│   │   │   ├── rtl.css.gz
│   │   │   ├── unusable_password_field.b433f2a95fba.css
│   │   │   ├── unusable_password_field.b433f2a95fba.css.gz
│   │   │   ├── unusable_password_field.css
│   │   │   ├── unusable_password_field.css.gz
│   │   │   ├── widgets.355d088349f3.css
│   │   │   ├── widgets.355d088349f3.css.gz
│   │   │   ├── widgets.css
│   │   │   └── widgets.css.gz
│   │   ├── img/
│   │   │   ├── gis/
│   │   │   │   ├── move_vertex_off.7a23bf31ef8a.svg
│   │   │   │   ├── move_vertex_off.7a23bf31ef8a.svg.gz
│   │   │   │   ├── move_vertex_off.svg
│   │   │   │   ├── move_vertex_off.svg.gz
│   │   │   │   ├── move_vertex_on.0047eba25b67.svg
│   │   │   │   ├── move_vertex_on.0047eba25b67.svg.gz
│   │   │   │   ├── move_vertex_on.svg
│   │   │   │   └── move_vertex_on.svg.gz
│   │   │   ├── calendar-icons.93ab098d1ac1.svg
│   │   │   ├── calendar-icons.93ab098d1ac1.svg.gz
│   │   │   ├── calendar-icons.svg
│   │   │   ├── calendar-icons.svg.gz
│   │   │   ├── icon-addlink.073aeb1feda7.svg
│   │   │   ├── icon-addlink.073aeb1feda7.svg.gz
│   │   │   ├── icon-addlink.svg
│   │   │   ├── icon-addlink.svg.gz
│   │   │   ├── icon-alert.034cc7d8a67f.svg
│   │   │   ├── icon-alert.034cc7d8a67f.svg.gz
│   │   │   ├── icon-alert.svg
│   │   │   ├── icon-alert.svg.gz
│   │   │   ├── icon-calendar.ac7aea671bea.svg
│   │   │   ├── icon-calendar.ac7aea671bea.svg.gz
│   │   │   ├── icon-calendar.svg
│   │   │   ├── icon-calendar.svg.gz
│   │   │   ├── icon-changelink.7eddb320e61f.svg
│   │   │   ├── icon-changelink.7eddb320e61f.svg.gz
│   │   │   ├── icon-changelink.svg
│   │   │   ├── icon-changelink.svg.gz
│   │   │   ├── icon-clock.e1d4dfac3f2b.svg
│   │   │   ├── icon-clock.e1d4dfac3f2b.svg.gz
│   │   │   ├── icon-clock.svg
│   │   │   ├── icon-clock.svg.gz
│   │   │   ├── icon-deletelink.564ef9dc3854.svg
│   │   │   ├── icon-deletelink.564ef9dc3854.svg.gz
│   │   │   ├── icon-deletelink.svg
│   │   │   ├── icon-deletelink.svg.gz
│   │   │   ├── icon-hidelink.8d245a995e18.svg
│   │   │   ├── icon-hidelink.8d245a995e18.svg.gz
│   │   │   ├── icon-hidelink.svg
│   │   │   ├── icon-hidelink.svg.gz
│   │   │   ├── icon-no.439e821418cd.svg
│   │   │   ├── icon-no.439e821418cd.svg.gz
│   │   │   ├── icon-no.svg
│   │   │   ├── icon-no.svg.gz
│   │   │   ├── icon-unknown-alt.81536e128bb6.svg
│   │   │   ├── icon-unknown-alt.81536e128bb6.svg.gz
│   │   │   ├── icon-unknown-alt.svg
│   │   │   ├── icon-unknown-alt.svg.gz
│   │   │   ├── icon-unknown.a18cb4398978.svg
│   │   │   ├── icon-unknown.a18cb4398978.svg.gz
│   │   │   ├── icon-unknown.svg
│   │   │   ├── icon-unknown.svg.gz
│   │   │   ├── icon-viewlink.41eb31f7826e.svg
│   │   │   ├── icon-viewlink.41eb31f7826e.svg.gz
│   │   │   ├── icon-viewlink.svg
│   │   │   ├── icon-viewlink.svg.gz
│   │   │   ├── icon-yes.d2f9f035226a.svg
│   │   │   ├── icon-yes.d2f9f035226a.svg.gz
│   │   │   ├── icon-yes.svg
│   │   │   ├── icon-yes.svg.gz
│   │   │   ├── inline-delete.fec1b761f254.svg
│   │   │   ├── inline-delete.fec1b761f254.svg.gz
│   │   │   ├── inline-delete.svg
│   │   │   ├── inline-delete.svg.gz
│   │   │   ├── LICENSE
│   │   │   ├── LICENSE.2c54f4e1ca1c
│   │   │   ├── LICENSE.2c54f4e1ca1c.gz
│   │   │   ├── LICENSE.gz
│   │   │   ├── README.9849248c9207.txt
│   │   │   ├── README.9849248c9207.txt.gz
│   │   │   ├── README.txt
│   │   │   ├── README.txt.gz
│   │   │   ├── search.7cf54ff789c6.svg
│   │   │   ├── search.7cf54ff789c6.svg.gz
│   │   │   ├── search.svg
│   │   │   ├── search.svg.gz
│   │   │   ├── selector-icons.b4555096cea2.svg
│   │   │   ├── selector-icons.b4555096cea2.svg.gz
│   │   │   ├── selector-icons.svg
│   │   │   ├── selector-icons.svg.gz
│   │   │   ├── sorting-icons.3a097b59f104.svg
│   │   │   ├── sorting-icons.3a097b59f104.svg.gz
│   │   │   ├── sorting-icons.svg
│   │   │   ├── sorting-icons.svg.gz
│   │   │   ├── tooltag-add.e59d620a9742.svg
│   │   │   ├── tooltag-add.e59d620a9742.svg.gz
│   │   │   ├── tooltag-add.svg
│   │   │   ├── tooltag-add.svg.gz
│   │   │   ├── tooltag-arrowright.bbfb788a849e.svg
│   │   │   ├── tooltag-arrowright.bbfb788a849e.svg.gz
│   │   │   ├── tooltag-arrowright.svg
│   │   │   └── tooltag-arrowright.svg.gz
│   │   └── js/
│   │       ├── admin/
│   │       │   ├── DateTimeShortcuts.9f6e209cebca.js
│   │       │   ├── DateTimeShortcuts.9f6e209cebca.js.gz
│   │       │   ├── DateTimeShortcuts.js
│   │       │   ├── DateTimeShortcuts.js.gz
│   │       │   ├── RelatedObjectLookups.874743a87811.js
│   │       │   ├── RelatedObjectLookups.874743a87811.js.gz
│   │       │   ├── RelatedObjectLookups.js
│   │       │   └── RelatedObjectLookups.js.gz
│   │       ├── vendor/
│   │       │   ├── jquery/
│   │       │   │   ├── jquery.12e87d2f3a4c.js
│   │       │   │   ├── jquery.12e87d2f3a4c.js.gz
│   │       │   │   ├── jquery.js
│   │       │   │   ├── jquery.js.gz
│   │       │   │   ├── jquery.min.2c872dbe60f4.js
│   │       │   │   ├── jquery.min.2c872dbe60f4.js.gz
│   │       │   │   ├── jquery.min.js
│   │       │   │   ├── jquery.min.js.gz
│   │       │   │   ├── LICENSE.de877aa6d744.txt
│   │       │   │   ├── LICENSE.de877aa6d744.txt.gz
│   │       │   │   ├── LICENSE.txt
│   │       │   │   └── LICENSE.txt.gz
│   │       │   ├── select2/
│   │       │   │   ├── i18n/
│   │       │   │   │   ├── af.4f6fcd73488c.js
│   │       │   │   │   ├── af.4f6fcd73488c.js.gz
│   │       │   │   │   ├── af.js
│   │       │   │   │   ├── af.js.gz
│   │       │   │   │   ├── ar.65aa8e36bf5d.js
│   │       │   │   │   ├── ar.65aa8e36bf5d.js.gz
│   │       │   │   │   ├── ar.js
│   │       │   │   │   ├── ar.js.gz
│   │       │   │   │   ├── az.270c257daf81.js
│   │       │   │   │   ├── az.270c257daf81.js.gz
│   │       │   │   │   ├── az.js
│   │       │   │   │   ├── az.js.gz
│   │       │   │   │   ├── bg.39b8be30d4f0.js
│   │       │   │   │   ├── bg.39b8be30d4f0.js.gz
│   │       │   │   │   ├── bg.js
│   │       │   │   │   ├── bg.js.gz
│   │       │   │   │   ├── bn.6d42b4dd5665.js
│   │       │   │   │   ├── bn.6d42b4dd5665.js.gz
│   │       │   │   │   ├── bn.js
│   │       │   │   │   ├── bn.js.gz
│   │       │   │   │   ├── bs.91624382358e.js
│   │       │   │   │   ├── bs.91624382358e.js.gz
│   │       │   │   │   ├── bs.js
│   │       │   │   │   ├── bs.js.gz
│   │       │   │   │   ├── ca.a166b745933a.js
│   │       │   │   │   ├── ca.a166b745933a.js.gz
│   │       │   │   │   ├── ca.js
│   │       │   │   │   ├── ca.js.gz
│   │       │   │   │   ├── cs.4f43e8e7d33a.js
│   │       │   │   │   ├── cs.4f43e8e7d33a.js.gz
│   │       │   │   │   ├── cs.js
│   │       │   │   │   ├── cs.js.gz
│   │       │   │   │   ├── da.766346afe4dd.js
│   │       │   │   │   ├── da.766346afe4dd.js.gz
│   │       │   │   │   ├── da.js
│   │       │   │   │   ├── da.js.gz
│   │       │   │   │   ├── de.8a1c222b0204.js
│   │       │   │   │   ├── de.8a1c222b0204.js.gz
│   │       │   │   │   ├── de.js
│   │       │   │   │   ├── de.js.gz
│   │       │   │   │   ├── dsb.56372c92d2f1.js
│   │       │   │   │   ├── dsb.56372c92d2f1.js.gz
│   │       │   │   │   ├── dsb.js
│   │       │   │   │   ├── dsb.js.gz
│   │       │   │   │   ├── el.27097f071856.js
│   │       │   │   │   ├── el.27097f071856.js.gz
│   │       │   │   │   ├── el.js
│   │       │   │   │   ├── el.js.gz
│   │       │   │   │   ├── en.cf932ba09a98.js
│   │       │   │   │   ├── en.cf932ba09a98.js.gz
│   │       │   │   │   ├── en.js
│   │       │   │   │   ├── en.js.gz
│   │       │   │   │   ├── es.66dbc2652fb1.js
│   │       │   │   │   ├── es.66dbc2652fb1.js.gz
│   │       │   │   │   ├── es.js
│   │       │   │   │   ├── es.js.gz
│   │       │   │   │   ├── et.2b96fd98289d.js
│   │       │   │   │   ├── et.2b96fd98289d.js.gz
│   │       │   │   │   ├── et.js
│   │       │   │   │   ├── et.js.gz
│   │       │   │   │   ├── eu.adfe5c97b72c.js
│   │       │   │   │   ├── eu.adfe5c97b72c.js.gz
│   │       │   │   │   ├── eu.js
│   │       │   │   │   ├── eu.js.gz
│   │       │   │   │   ├── fa.3b5bd1961cfd.js
│   │       │   │   │   ├── fa.3b5bd1961cfd.js.gz
│   │       │   │   │   ├── fa.js
│   │       │   │   │   ├── fa.js.gz
│   │       │   │   │   ├── fi.614ec42aa9ba.js
│   │       │   │   │   ├── fi.614ec42aa9ba.js.gz
│   │       │   │   │   ├── fi.js
│   │       │   │   │   ├── fi.js.gz
│   │       │   │   │   ├── fr.05e0542fcfe6.js
│   │       │   │   │   ├── fr.05e0542fcfe6.js.gz
│   │       │   │   │   ├── fr.js
│   │       │   │   │   ├── fr.js.gz
│   │       │   │   │   ├── gl.d99b1fedaa86.js
│   │       │   │   │   ├── gl.d99b1fedaa86.js.gz
│   │       │   │   │   ├── gl.js
│   │       │   │   │   ├── gl.js.gz
│   │       │   │   │   ├── he.e420ff6cd3ed.js
│   │       │   │   │   ├── he.e420ff6cd3ed.js.gz
│   │       │   │   │   ├── he.js
│   │       │   │   │   ├── he.js.gz
│   │       │   │   │   ├── hi.70640d41628f.js
│   │       │   │   │   ├── hi.70640d41628f.js.gz
│   │       │   │   │   ├── hi.js
│   │       │   │   │   ├── hi.js.gz
│   │       │   │   │   ├── hr.a2b092cc1147.js
│   │       │   │   │   ├── hr.a2b092cc1147.js.gz
│   │       │   │   │   ├── hr.js
│   │       │   │   │   ├── hr.js.gz
│   │       │   │   │   ├── hsb.fa3b55265efe.js
│   │       │   │   │   ├── hsb.fa3b55265efe.js.gz
│   │       │   │   │   ├── hsb.js
│   │       │   │   │   ├── hsb.js.gz
│   │       │   │   │   ├── hu.6ec6039cb8a3.js
│   │       │   │   │   ├── hu.6ec6039cb8a3.js.gz
│   │       │   │   │   ├── hu.js
│   │       │   │   │   ├── hu.js.gz
│   │       │   │   │   ├── hy.c7babaeef5a6.js
│   │       │   │   │   ├── hy.c7babaeef5a6.js.gz
│   │       │   │   │   ├── hy.js
│   │       │   │   │   ├── hy.js.gz
│   │       │   │   │   ├── id.04debded514d.js
│   │       │   │   │   ├── id.04debded514d.js.gz
│   │       │   │   │   ├── id.js
│   │       │   │   │   ├── id.js.gz
│   │       │   │   │   ├── is.3ddd9a6a97e9.js
│   │       │   │   │   ├── is.3ddd9a6a97e9.js.gz
│   │       │   │   │   ├── is.js
│   │       │   │   │   ├── is.js.gz
│   │       │   │   │   ├── it.be4fe8d365b5.js
│   │       │   │   │   ├── it.be4fe8d365b5.js.gz
│   │       │   │   │   ├── it.js
│   │       │   │   │   ├── it.js.gz
│   │       │   │   │   ├── ja.170ae885d74f.js
│   │       │   │   │   ├── ja.170ae885d74f.js.gz
│   │       │   │   │   ├── ja.js
│   │       │   │   │   ├── ja.js.gz
│   │       │   │   │   ├── ka.2083264a54f0.js
│   │       │   │   │   ├── ka.2083264a54f0.js.gz
│   │       │   │   │   ├── ka.js
│   │       │   │   │   ├── ka.js.gz
│   │       │   │   │   ├── km.c23089cb06ca.js
│   │       │   │   │   ├── km.c23089cb06ca.js.gz
│   │       │   │   │   ├── km.js
│   │       │   │   │   ├── km.js.gz
│   │       │   │   │   ├── ko.e7be6c20e673.js
│   │       │   │   │   ├── ko.e7be6c20e673.js.gz
│   │       │   │   │   ├── ko.js
│   │       │   │   │   ├── ko.js.gz
│   │       │   │   │   ├── lt.23c7ce903300.js
│   │       │   │   │   ├── lt.23c7ce903300.js.gz
│   │       │   │   │   ├── lt.js
│   │       │   │   │   ├── lt.js.gz
│   │       │   │   │   ├── lv.08e62128eac1.js
│   │       │   │   │   ├── lv.08e62128eac1.js.gz
│   │       │   │   │   ├── lv.js
│   │       │   │   │   ├── lv.js.gz
│   │       │   │   │   ├── mk.dabbb9087130.js
│   │       │   │   │   ├── mk.dabbb9087130.js.gz
│   │       │   │   │   ├── mk.js
│   │       │   │   │   ├── mk.js.gz
│   │       │   │   │   ├── ms.4ba82c9a51ce.js
│   │       │   │   │   ├── ms.4ba82c9a51ce.js.gz
│   │       │   │   │   ├── ms.js
│   │       │   │   │   ├── ms.js.gz
│   │       │   │   │   ├── nb.da2fce143f27.js
│   │       │   │   │   ├── nb.da2fce143f27.js.gz
│   │       │   │   │   ├── nb.js
│   │       │   │   │   ├── nb.js.gz
│   │       │   │   │   ├── ne.3d79fd3f08db.js
│   │       │   │   │   ├── ne.3d79fd3f08db.js.gz
│   │       │   │   │   ├── ne.js
│   │       │   │   │   ├── ne.js.gz
│   │       │   │   │   ├── nl.997868a37ed8.js
│   │       │   │   │   ├── nl.997868a37ed8.js.gz
│   │       │   │   │   ├── nl.js
│   │       │   │   │   ├── nl.js.gz
│   │       │   │   │   ├── pl.6031b4f16452.js
│   │       │   │   │   ├── pl.6031b4f16452.js.gz
│   │       │   │   │   ├── pl.js
│   │       │   │   │   ├── pl.js.gz
│   │       │   │   │   ├── ps.38dfa47af9e0.js
│   │       │   │   │   ├── ps.38dfa47af9e0.js.gz
│   │       │   │   │   ├── ps.js
│   │       │   │   │   ├── ps.js.gz
│   │       │   │   │   ├── pt-BR.e1b294433e7f.js
│   │       │   │   │   ├── pt-BR.e1b294433e7f.js.gz
│   │       │   │   │   ├── pt-BR.js
│   │       │   │   │   ├── pt-BR.js.gz
│   │       │   │   │   ├── pt.33b4a3b44d43.js
│   │       │   │   │   ├── pt.33b4a3b44d43.js.gz
│   │       │   │   │   ├── pt.js
│   │       │   │   │   ├── pt.js.gz
│   │       │   │   │   ├── ro.f75cb460ec3b.js
│   │       │   │   │   ├── ro.f75cb460ec3b.js.gz
│   │       │   │   │   ├── ro.js
│   │       │   │   │   ├── ro.js.gz
│   │       │   │   │   ├── ru.934aa95f5b5f.js
│   │       │   │   │   ├── ru.934aa95f5b5f.js.gz
│   │       │   │   │   ├── ru.js
│   │       │   │   │   ├── ru.js.gz
│   │       │   │   │   ├── sk.33d02cef8d11.js
│   │       │   │   │   ├── sk.33d02cef8d11.js.gz
│   │       │   │   │   ├── sk.js
│   │       │   │   │   ├── sk.js.gz
│   │       │   │   │   ├── sl.131a78bc0752.js
│   │       │   │   │   ├── sl.131a78bc0752.js.gz
│   │       │   │   │   ├── sl.js
│   │       │   │   │   ├── sl.js.gz
│   │       │   │   │   ├── sq.5636b60d29c9.js
│   │       │   │   │   ├── sq.5636b60d29c9.js.gz
│   │       │   │   │   ├── sq.js
│   │       │   │   │   ├── sq.js.gz
│   │       │   │   │   ├── sr-Cyrl.f254bb8c4c7c.js
│   │       │   │   │   ├── sr-Cyrl.f254bb8c4c7c.js.gz
│   │       │   │   │   ├── sr-Cyrl.js
│   │       │   │   │   ├── sr-Cyrl.js.gz
│   │       │   │   │   ├── sr.5ed85a48f483.js
│   │       │   │   │   ├── sr.5ed85a48f483.js.gz
│   │       │   │   │   ├── sr.js
│   │       │   │   │   ├── sr.js.gz
│   │       │   │   │   ├── sv.7a9c2f71e777.js
│   │       │   │   │   ├── sv.7a9c2f71e777.js.gz
│   │       │   │   │   ├── sv.js
│   │       │   │   │   ├── sv.js.gz
│   │       │   │   │   ├── th.f38c20b0221b.js
│   │       │   │   │   ├── th.f38c20b0221b.js.gz
│   │       │   │   │   ├── th.js
│   │       │   │   │   ├── th.js.gz
│   │       │   │   │   ├── tk.7c572a68c78f.js
│   │       │   │   │   ├── tk.7c572a68c78f.js.gz
│   │       │   │   │   ├── tk.js
│   │       │   │   │   ├── tk.js.gz
│   │       │   │   │   ├── tr.b5a0643d1545.js
│   │       │   │   │   ├── tr.b5a0643d1545.js.gz
│   │       │   │   │   ├── tr.js
│   │       │   │   │   ├── tr.js.gz
│   │       │   │   │   ├── uk.8cede7f4803c.js
│   │       │   │   │   ├── uk.8cede7f4803c.js.gz
│   │       │   │   │   ├── uk.js
│   │       │   │   │   ├── uk.js.gz
│   │       │   │   │   ├── vi.097a5b75b3e1.js
│   │       │   │   │   ├── vi.097a5b75b3e1.js.gz
│   │       │   │   │   ├── vi.js
│   │       │   │   │   ├── vi.js.gz
│   │       │   │   │   ├── zh-CN.2cff662ec5f9.js
│   │       │   │   │   ├── zh-CN.2cff662ec5f9.js.gz
│   │       │   │   │   ├── zh-CN.js
│   │       │   │   │   ├── zh-CN.js.gz
│   │       │   │   │   ├── zh-TW.04554a227c2b.js
│   │       │   │   │   ├── zh-TW.04554a227c2b.js.gz
│   │       │   │   │   ├── zh-TW.js
│   │       │   │   │   └── zh-TW.js.gz
│   │       │   │   ├── LICENSE.f94142512c91.md
│   │       │   │   ├── LICENSE.f94142512c91.md.gz
│   │       │   │   ├── LICENSE.md
│   │       │   │   ├── LICENSE.md.gz
│   │       │   │   ├── select2.full.c2afdeda3058.js
│   │       │   │   ├── select2.full.c2afdeda3058.js.gz
│   │       │   │   ├── select2.full.js
│   │       │   │   ├── select2.full.js.gz
│   │       │   │   ├── select2.full.min.fcd7500d8e13.js
│   │       │   │   ├── select2.full.min.fcd7500d8e13.js.gz
│   │       │   │   ├── select2.full.min.js
│   │       │   │   └── select2.full.min.js.gz
│   │       │   └── xregexp/
│   │       │       ├── LICENSE.b6fd2ceea8d3.txt
│   │       │       ├── LICENSE.b6fd2ceea8d3.txt.gz
│   │       │       ├── LICENSE.txt
│   │       │       ├── LICENSE.txt.gz
│   │       │       ├── xregexp.a7e08b0ce686.js
│   │       │       ├── xregexp.a7e08b0ce686.js.gz
│   │       │       ├── xregexp.js
│   │       │       ├── xregexp.js.gz
│   │       │       ├── xregexp.min.f1ae4617847c.js
│   │       │       ├── xregexp.min.f1ae4617847c.js.gz
│   │       │       ├── xregexp.min.js
│   │       │       └── xregexp.min.js.gz
│   │       ├── actions.f1d5653edb59.js
│   │       ├── actions.f1d5653edb59.js.gz
│   │       ├── actions.js
│   │       ├── actions.js.gz
│   │       ├── autocomplete.01591ab27be7.js
│   │       ├── autocomplete.01591ab27be7.js.gz
│   │       ├── autocomplete.js
│   │       ├── autocomplete.js.gz
│   │       ├── calendar.d64496bbf46d.js
│   │       ├── calendar.d64496bbf46d.js.gz
│   │       ├── calendar.js
│   │       ├── calendar.js.gz
│   │       ├── cancel.ecc4c5ca7b32.js
│   │       ├── cancel.ecc4c5ca7b32.js.gz
│   │       ├── cancel.js
│   │       ├── cancel.js.gz
│   │       ├── change_form.9d8ca4f96b75.js
│   │       ├── change_form.9d8ca4f96b75.js.gz
│   │       ├── change_form.js
│   │       ├── change_form.js.gz
│   │       ├── core.7e257fdf56dc.js
│   │       ├── core.7e257fdf56dc.js.gz
│   │       ├── core.js
│   │       ├── core.js.gz
│   │       ├── filters.0e360b7a9f80.js
│   │       ├── filters.0e360b7a9f80.js.gz
│   │       ├── filters.js
│   │       ├── filters.js.gz
│   │       ├── inlines.22d4d93c00b4.js
│   │       ├── inlines.22d4d93c00b4.js.gz
│   │       ├── inlines.js
│   │       ├── inlines.js.gz
│   │       ├── jquery.init.b7781a0897fc.js
│   │       ├── jquery.init.b7781a0897fc.js.gz
│   │       ├── jquery.init.js
│   │       ├── jquery.init.js.gz
│   │       ├── nav_sidebar.3b9190d420b1.js
│   │       ├── nav_sidebar.3b9190d420b1.js.gz
│   │       ├── nav_sidebar.js
│   │       ├── nav_sidebar.js.gz
│   │       ├── popup_response.96190d343c22.js
│   │       ├── popup_response.96190d343c22.js.gz
│   │       ├── popup_response.js
│   │       ├── popup_response.js.gz
│   │       ├── prepopulate.bd2361dfd64d.js
│   │       ├── prepopulate.bd2361dfd64d.js.gz
│   │       ├── prepopulate.js
│   │       ├── prepopulate.js.gz
│   │       ├── prepopulate_init.6cac7f3105b8.js
│   │       ├── prepopulate_init.6cac7f3105b8.js.gz
│   │       ├── prepopulate_init.js
│   │       ├── prepopulate_init.js.gz
│   │       ├── SelectBox.7d3ce5a98007.js
│   │       ├── SelectBox.7d3ce5a98007.js.gz
│   │       ├── SelectBox.js
│   │       ├── SelectBox.js.gz
│   │       ├── SelectFilter2.b20260d34877.js
│   │       ├── SelectFilter2.b20260d34877.js.gz
│   │       ├── SelectFilter2.js
│   │       ├── SelectFilter2.js.gz
│   │       ├── theme.91cf832f559e.js
│   │       ├── theme.91cf832f559e.js.gz
│   │       ├── theme.js
│   │       ├── theme.js.gz
│   │       ├── unusable_password_field.017ea86b6ae4.js
│   │       ├── unusable_password_field.017ea86b6ae4.js.gz
│   │       ├── unusable_password_field.js
│   │       ├── unusable_password_field.js.gz
│   │       ├── urlify.ae970a820212.js
│   │       ├── urlify.ae970a820212.js.gz
│   │       ├── urlify.js
│   │       └── urlify.js.gz
│   ├── django_classified/
│   │   ├── css/
│   │   │   ├── bootstrap.min.ac6c32a27bd7.css
│   │   │   ├── bootstrap.min.ac6c32a27bd7.css.gz
│   │   │   ├── bootstrap.min.css
│   │   │   ├── bootstrap.min.css.d2fc5925f2dc.map
│   │   │   ├── bootstrap.min.css.d2fc5925f2dc.map.gz
│   │   │   ├── bootstrap.min.css.gz
│   │   │   ├── bootstrap.min.css.map
│   │   │   ├── bootstrap.min.css.map.gz
│   │   │   ├── jumbotron-narrow.6bb79fe6e3e1.css
│   │   │   ├── jumbotron-narrow.6bb79fe6e3e1.css.gz
│   │   │   ├── jumbotron-narrow.css
│   │   │   ├── jumbotron-narrow.css.gz
│   │   │   ├── lightbox.min.css
│   │   │   ├── lightbox.min.css.gz
│   │   │   ├── lightbox.min.f6bde759aa9f.css
│   │   │   ├── lightbox.min.f6bde759aa9f.css.gz
│   │   │   ├── style.55646fc1c986.css
│   │   │   └── style.css
│   │   ├── fonts/
│   │   │   ├── glyphicons-halflings-regular.448c34a56d69.woff2
│   │   │   ├── glyphicons-halflings-regular.7ced3229845a.svg
│   │   │   ├── glyphicons-halflings-regular.7ced3229845a.svg.gz
│   │   │   ├── glyphicons-halflings-regular.e18bbf611f2a.ttf
│   │   │   ├── glyphicons-halflings-regular.e18bbf611f2a.ttf.gz
│   │   │   ├── glyphicons-halflings-regular.eot
│   │   │   ├── glyphicons-halflings-regular.f4769f9bdb74.eot
│   │   │   ├── glyphicons-halflings-regular.fa2772327f55.woff
│   │   │   ├── glyphicons-halflings-regular.svg
│   │   │   ├── glyphicons-halflings-regular.svg.gz
│   │   │   ├── glyphicons-halflings-regular.ttf
│   │   │   ├── glyphicons-halflings-regular.ttf.gz
│   │   │   ├── glyphicons-halflings-regular.woff
│   │   │   └── glyphicons-halflings-regular.woff2
│   │   ├── images/
│   │   │   ├── close.d9d2d0b1308c.png
│   │   │   ├── close.png
│   │   │   ├── favicon.7d085f80dbea.ico
│   │   │   ├── favicon.7d085f80dbea.ico.gz
│   │   │   ├── favicon.ico
│   │   │   ├── favicon.ico.gz
│   │   │   ├── loading.2299ad0b3f63.gif
│   │   │   ├── loading.gif
│   │   │   ├── next.31f15875975a.png
│   │   │   ├── next.png
│   │   │   ├── prev.84b76dee6b27.png
│   │   │   └── prev.png
│   │   └── js/
│   │       ├── bootstrap.min.5869c96cc8f1.js
│   │       ├── bootstrap.min.5869c96cc8f1.js.gz
│   │       ├── bootstrap.min.js
│   │       ├── bootstrap.min.js.gz
│   │       ├── jquery-3.3.1.min.a09e13ee94d5.js
│   │       ├── jquery-3.3.1.min.a09e13ee94d5.js.gz
│   │       ├── jquery-3.3.1.min.js
│   │       ├── jquery-3.3.1.min.js.gz
│   │       ├── lightbox.min.0ce1c728cb2f.map
│   │       ├── lightbox.min.0ce1c728cb2f.map.gz
│   │       ├── lightbox.min.d5bfc35092c9.js
│   │       ├── lightbox.min.d5bfc35092c9.js.gz
│   │       ├── lightbox.min.js
│   │       ├── lightbox.min.js.gz
│   │       ├── lightbox.min.map
│   │       └── lightbox.min.map.gz
│   └── staticfiles.json
├── templates/
│   ├── cloudinary/
│   │   └── image_gallery.html
│   ├── django_classified/
│   │   ├── _base.html
│   │   ├── item_detail.html
│   │   ├── item_form.html
│   │   ├── item_list.html
│   │   ├── login.html
│   │   ├── password_reset_complete.html
│   │   ├── password_reset_confirm.html
│   │   ├── password_reset_done.html
│   │   ├── password_reset_email.txt
│   │   ├── password_reset_form.html
│   │   ├── password_reset_subject.txt
│   │   ├── profile.html
│   │   ├── search.html
│   │   └── section_list.html
│   ├── payments/
│   │   ├── payment_cancelled.html
│   │   ├── payment_success.html
│   │   ├── purchase_history.html
│   │   ├── request_detail.html
│   │   ├── request_purchase.html
│   │   ├── sales_history.html
│   │   ├── seller_requests.html
│   │   ├── seller_setup.html
│   │   ├── template_seller_setup.html
│   │   └── transaction_detail.html
│   ├── registration/
│   │   ├── registration_complete.html
│   │   └── registration_form.html
│   ├── trade/
│   │   ├── detail.html
│   │   ├── inbox.html
│   │   ├── propose.html
│   │   ├── sent.html
│   │   └── user_profile.html
│   ├── base.html
│   └── debug_cloudinary.html
├── trade/
│   ├── management/
│   │   ├── commands/
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── mangement/
│   │   ├── commands/
│   │   │   ├── __init__.py
│   │   │   └── create_user_profiles.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── user_profile.py
│   └── views.py
├── __init__.py
├── app.json
├── baratto.ps1
├── customize_templates.py
├── db.sqlite3
├── deb_pur.py
├── fix_templates.py
├── LICENSE
├── list_html.txt
├── list_py.txt
├── manage.py
├── Procfile
├── proj_snapshot.py
├── README.md
├── README_CLOUDINARY.md
├── requirements.txt
├── runtime.txt
├── setup_site.py
└── wsgi.py
```


---

## Recently Changed Files (last 3h)


### proj_snapshot.py

```python
#!/usr/bin/env python3
# proj_snapshot.py — Crea un CONTEXT.md conciso del progetto Django
# con opzionale storia Git, snapshot template, estratti file chiave,
# albero directory e (NOVITÀ) sezione "Recently Changed Files".
#
# Esempi:
#   python proj_snapshot.py --templates interesting
#   python proj_snapshot.py --templates all --templates-max-file-lines 400
#   python proj_snapshot.py --templates all --recent-hours 6
#   python proj_snapshot.py --recent-hours 0  # disattiva "recenti"

from __future__ import annotations
import os
import re
import sys
import argparse
import textwrap
import pathlib
import subprocess
import shutil
from datetime import datetime, timedelta
from typing import List, Literal, Iterable

# ---------- Configurazione di base ----------

DEFAULT_OUT_DIR = "out"
DEFAULT_MAX_LINES = 5000
DEFAULT_MAX_FILE_LINES = 300
DEFAULT_HTML_MAX_FILE_LINES = 300
DEFAULT_GIT_MAX = 50
RECENT_MAX_FILES = 100  # tetto di sicurezza per la sezione "recenti"

# Directory escluse dal walk del progetto
EXCLUDED_DIRS = {
    ".git", ".hg", ".svn", ".idea", ".vscode", "__pycache__",
    "node_modules", "dist", "build", "staticfiles", "media",
    ".venv", "venv", "env", ".mypy_cache", ".pytest_cache", ".ruff_cache",
    ".tox", ".coverage", "coverage", "htmlcov", "site-packages",
    "migrations"  # di solito poco utili nello snapshot
}

# File di app considerati "core"
APP_CODE_FILES = {
    "models.py", "views.py", "urls.py", "forms.py", "admin.py",
    "serializers.py", "apps.py", "signals.py", "permissions.py",
    "tasks.py", "consumers.py", "selectors.py", "services.py"
}

# App "di interesse" (adatta ai tuoi nomi reali)
PRIMARY_APP_NAMES = {"trade", "payments"}
MSG_APP_NAMES = {"messaging", "chat", "inbox"}
USER_APP_NAMES = {"users", "accounts", "profiles"}

TemplatesMode = Literal["all", "interesting", "none"]

# Parole chiave per "templates interesting"
TEMPLATE_KEYWORDS = (
    "login", "password_reset", "registration", "email_sent", "_base", "base",
    "trade", "account", "signup", "logout", "profile",
    "conversation", "message", "chat", "inbox"
)

# ---------- Redaction credenziali & segreti ----------

REDACTIONS = [
    # Django SECRET_KEY = '***REDACTED***'
    (re.compile(r"(SECRET_KEY\s*=\s*)([\"'])(?P<val>.+?)(\2)"), r"\1'***REDACTED***'"),
    # Social auth / variabili "URL"
    (re.compile(r"(SOCIAL_AUTH_[A-Z0-9_]+?\s*=\s*)([\"']?)(?P<val>[^\"'\n]+)([\"']?)"), r"\1'***REDACTED***'"),
    # os.environ.get("FOO", '***REDACTED***') → redazione del default
    (re.compile(r"os\.environ\.get\(\s*([\"'][A-Z0-9_]+[\"'])\s*,\s*([\"'])(?P<val>.+?)(\2)\s*\)"),
     r"os.environ.get(\1, '***REDACTED***')"),
    # DATABASE_URL / EMAIL_URL='***REDACTED***'
    (re.compile(r"(DATABASE_URL|EMAIL_URL)\s*=\s*([\"'])(?P<val>.+?)(\2)"), r"\1='***REDACTED***'"),
    # qualsiasi PASSWORD = '***REDACTED***'
    (re.compile(r"(?i)(PASSWORD\s*=\s*)([\"'])(?P<val>.+?)(\2)"), r"\1'***REDACTED***'"),
    # Cloudinary URL
    (re.compile(r"(CLOUDINARY_URL\s*=\s*)([\"'])(?P<val>.+?)(\2)"), r"\1'***REDACTED***'"),
]

def redact(text: str) -> str:
    for pat, repl in REDACTIONS:
        text = pat.sub(repl, text)
    return text

# ---------- Utility di identificazione file ----------

def is_excluded_dir(rel_path: pathlib.Path) -> bool:
    """
    Ritorna True se una delle parti della path è in EXCLUDED_DIRS.
    """
    for part in rel_path.parts:
        if part in EXCLUDED_DIRS:
            return True
    return False

def is_template(path: pathlib.Path) -> bool:
    return path.suffix.lower() == ".html"

def is_code_file(path: pathlib.Path) -> bool:
    if path.suffix.lower() in {".py", ".js", ".ts", ".css", ".json", ".yaml", ".yml", ".ini", ".cfg", ".toml", ".env", ".txt", ".md"}:
        return True
    # include anche manage.py, wsgi, asgi, settings
    name = path.name
    if name in {"manage.py", "wsgi.py", "asgi.py"}:
        return True
    return False

def is_app_code_file(path: pathlib.Path) -> bool:
    return path.name in APP_CODE_FILES

def template_is_interesting(path: pathlib.Path) -> bool:
    if not is_template(path):
        return False
    name = path.name.lower()
    if any(k in name for k in TEMPLATE_KEYWORDS):
        return True
    parts = {p.lower() for p in path.parts}
    if "templates" in parts:
        if (PRIMARY_APP_NAMES | MSG_APP_NAMES | USER_APP_NAMES) & parts:
            return True
    return False

# ---------- Walk progetto ----------

def iter_files(root: pathlib.Path) -> Iterable[pathlib.Path]:
    for p in root.rglob("*"):
        if p.is_dir():
            continue
        yield p

def collect_template_files(root: pathlib.Path, mode: TemplatesMode) -> List[pathlib.Path]:
    if mode == "none":
        return []
    files: List[pathlib.Path] = []
    for p in iter_files(root):
        rel = p.relative_to(root)
        if is_excluded_dir(rel.parent):
            continue
        if not is_template(p):
            continue
        if mode == "all":
            files.append(p)
        elif mode == "interesting":
            if template_is_interesting(p):
                files.append(p)
    # Ordina per path
    files.sort(key=lambda x: x.as_posix().lower())
    return files

def collect_candidate_files(root: pathlib.Path, templates_mode: TemplatesMode) -> List[pathlib.Path]:
    """
    Raccoglie:
    - settings.py, urls.py, asgi.py, wsgi.py, manage.py
    - file core delle app (models/views/urls/..)
    - altri file 'interessanti' non-HTML
    NOTA: i template sono gestiti separatamente.
    """
    wanted_names = {"settings.py", "urls.py", "asgi.py", "wsgi.py", "manage.py"}
    files: List[pathlib.Path] = []
    for p in iter_files(root):
        rel = p.relative_to(root)
        if is_excluded_dir(rel.parent):
            continue
        if is_template(p):
            continue  # templates gestiti a parte
        if p.name in wanted_names or is_app_code_file(p) or p.suffix.lower() in {".py", ".ini", ".cfg", ".toml", ".yaml", ".yml"}:
            files.append(p)
    files.sort(key=lambda x: x.as_posix().lower())
    return files

# ---------- Sezione "recenti" ----------

def _best_changed_dt(p: pathlib.Path) -> datetime:
    try:
        st = p.stat()
    except Exception:
        return datetime.fromtimestamp(0)
    ts = getattr(st, "st_mtime", None)
    if ts is None:
        return datetime.fromtimestamp(0)
    return datetime.fromtimestamp(ts)

def collect_recent_files(root: pathlib.Path, hours: int) -> List[pathlib.Path]:
    if not hours or hours <= 0:
        return []
    cutoff = datetime.now() - timedelta(hours=hours)
    recent: List[pathlib.Path] = []
    for p in iter_files(root):
        rel = p.relative_to(root)
        if is_excluded_dir(rel.parent):
            continue
        if not (is_code_file(p) or is_template(p)):
            continue
        if _best_changed_dt(p) >= cutoff:
            recent.append(p)
            if len(recent) >= RECENT_MAX_FILES:
                break
    # Dedup + ordine per path
    seen = set()
    ordered: List[pathlib.Path] = []
    for f in sorted(recent, key=lambda x: x.as_posix().lower()):
        rp = f.as_posix()
        if rp not in seen:
            seen.add(rp)
            ordered.append(f)
    return ordered

# ---------- Lettura file & tree ----------

def read_file_excerpt(path: pathlib.Path, max_file_lines: int) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return f"<<unable to read: {e}>>"
    text = redact(text)
    lines = text.splitlines()
    truncated = False
    if len(lines) > max_file_lines:
        lines = lines[:max_file_lines]
        truncated = True
    out = "\n".join(lines)
    if truncated:
        out += f"\n\n<<TRUNCATED FILE: limited to {max_file_lines} lines>>"
    return out

def build_tree(root: pathlib.Path) -> str:
    """
    Tree semplice tipo:
    project/
    ├── app/
    │   ├── models.py
    │   └── views.py
    └── manage.py
    """
    lines: List[str] = []

    def listdir_filtered(dir_path: pathlib.Path) -> List[pathlib.Path]:
        try:
            entries = [
                e for e in sorted(dir_path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
                if not (is_excluded_dir(e.relative_to(root)) or e.name.startswith("."))
            ]
        except Exception:
            return []
        return entries

    def walk(dir_path: pathlib.Path, depth: int, prefix_stack: List[str]):
        entries = listdir_filtered(dir_path)
        for i, e in enumerate(entries):
            last = (i == len(entries) - 1)
            branch = "└── " if last else "├── "
            prefix = "".join(prefix_stack) + branch
            if e.is_dir():
                lines.append(f"{prefix}{e.name}/")
                prefix_stack.append("    " if last else "│   ")
                walk(e, depth + 1, prefix_stack)
                prefix_stack.pop()
            else:
                lines.append(f"{prefix}{e.name}")

    lines.append(root.resolve().name + "/")
    walk(root, 1, [])
    return "\n".join(lines)

# ---------- Storia Git ----------

def collect_git_history(root: pathlib.Path, max_commits: int) -> str:
    git_dir = root / ".git"
    if not git_dir.exists():
        return ""
    try:
        cmd = ["git", "-C", str(root), "log", f"-{max_commits}", "--oneline", "--decorate", "--graph", "--date=short", "--pretty=format:%h %ad %d %s"]
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        return out.strip()
    except Exception as e:
        return f"<<Unable to read git history: {e}>>"

# ---------- Main ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_OUT_DIR, help="Output directory (default: out)")
    ap.add_argument("--max-lines", type=int, default=DEFAULT_MAX_LINES, help="Max total lines in CONTEXT.md")
    ap.add_argument("--max-file-lines", type=int, default=DEFAULT_MAX_FILE_LINES, help="Max lines per non-HTML file excerpt")
    ap.add_argument("--templates-max-file-lines", type=int, default=DEFAULT_HTML_MAX_FILE_LINES, help="Max lines per HTML template excerpt")
    ap.add_argument("--git-max", type=int, default=DEFAULT_GIT_MAX, help="Max number of git commits to include (0 to disable)")
    ap.add_argument("--templates", choices=["all", "interesting", "none"], default="interesting",
                    help="Which templates to include")
    ap.add_argument("--recent-hours", type=int, default=3,
                    help="Include files changed in the last N hours (0 to disable). Default: 3")
    args = ap.parse_args()

    root = pathlib.Path(".").resolve()
    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    context_md = out_dir / "CONTEXT.md"
    doc_parts: List[str] = []


<<TRUNCATED FILE: limited to 300 lines>>
```


### project/__init__.py

```python

default_app_config = 'project.apps.ProjectConfig'
```


### project/apps.py

```python
from django.apps import AppConfig


class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'
    verbose_name = 'NINVENDO Project Core'
    
    def ready(self):
        """
        Codice da eseguire quando l'app è pronta
        """
        # Import dei signal handlers Cloudinary (solo in produzione)
        from django.conf import settings
        
        if not getattr(settings, 'DEBUG', True):
            try:
                import project.cloudinary_signals
                print("📷 Cloudinary signals registrati")
            except ImportError as e:
                print(f"⚠️ Impossibile registrare Cloudinary signals: {e}")
```


### project/cloudinary_signals.py

```python
"""
Signal handlers per gestire automaticamente upload/eliminazione immagini su Cloudinary
"""
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.conf import settings
import os
import logging

# Import dei modelli che hanno immagini
try:
    from django_classified.models import Item, ItemImage  # Se esiste un modello ItemImage
except ImportError:
    # Se non esiste ItemImage, usiamo solo Item
    from django_classified.models import Item
    ItemImage = None

from trade.models import TradeMessage  # Per le immagini nei messaggi

from .cloudinary_utils import (
    upload_image_to_cloudinary,
    delete_cloudinary_image,
    is_cloudinary_configured
)

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Item)
def handle_item_image_upload(sender, instance, created, **kwargs):
    """
    Gestisce upload automatico dell'immagine principale quando viene salvato un Item
    """
    if not is_cloudinary_configured():
        return
    
    # Solo in produzione (non in debug)
    if settings.DEBUG:
        return
    
    try:
        # Se c'è un'immagine e non è ancora stata processata
        if hasattr(instance, 'image') and instance.image:
            # Controlla se l'immagine è stata appena caricata
            if created or not hasattr(instance, '_cloudinary_processed'):
                
                # Genera public_id univoco
                public_id = f"items/item_{instance.pk}_{instance.slug}"
                
                # Upload su Cloudinary
                result = upload_image_to_cloudinary(
                    instance.image.file,
                    folder="items",
                    public_id=public_id
                )
                
                if result:
                    # Marca come processato
                    instance._cloudinary_processed = True
                    logger.info(f"Immagine Item {instance.pk} caricata su Cloudinary: {result['public_id']}")
                else:
                    logger.warning(f"Fallito upload Cloudinary per Item {instance.pk}")
                    
    except Exception as e:
        logger.error(f"Errore signal handler Item image delete: {e}")


@receiver(post_save, sender=TradeMessage)
def handle_trade_message_image_upload(sender, instance, created, **kwargs):
    """
    Gestisce upload automatico delle immagini nei messaggi di scambio
    """
    if not is_cloudinary_configured():
        return
    
    if settings.DEBUG:
        return
    
    try:
        # Se c'è un'immagine e il messaggio è appena stato creato
        if created and hasattr(instance, 'image') and instance.image:
            
            # Genera public_id univoco per il messaggio
            public_id = f"trade_messages/trade_{instance.trade.pk}/msg_{instance.pk}"
            
            # Upload su Cloudinary
            result = upload_image_to_cloudinary(
                instance.image.file,
                folder="trade_messages",
                public_id=public_id
            )
            
            if result:
                logger.info(f"Immagine TradeMessage {instance.pk} caricata su Cloudinary: {result['public_id']}")
            else:
                logger.warning(f"Fallito upload Cloudinary per TradeMessage {instance.pk}")
                
    except Exception as e:
        logger.error(f"Errore signal handler TradeMessage image upload: {e}")


@receiver(post_delete, sender=TradeMessage)
def handle_trade_message_image_delete(sender, instance, **kwargs):
    """
    Elimina immagine da Cloudinary quando viene eliminato un TradeMessage
    """
    if not is_cloudinary_configured():
        return
    
    if settings.DEBUG:
        return
    
    try:
        if hasattr(instance, 'image') and instance.image:
            # Ricostruisci public_id
            public_id = f"ninvendo/trade_messages/trade_{instance.trade.pk}/msg_{instance.pk}"
            
            success = delete_cloudinary_image(public_id)
            
            if success:
                logger.info(f"Immagine TradeMessage {instance.pk} eliminata da Cloudinary")
            else:
                logger.warning(f"Impossibile eliminare immagine TradeMessage {instance.pk} da Cloudinary")
                
    except Exception as e:
        logger.error(f"Errore signal handler TradeMessage image delete: {e}")


# Signal handler generico per modelli con immagini multiple (se necessario)
if ItemImage:  # Se esiste un modello per immagini multiple
    
    @receiver(post_save, sender=ItemImage)
    def handle_item_image_multiple_upload(sender, instance, created, **kwargs):
        """
        Gestisce upload di immagini multiple per un Item
        """
        if not is_cloudinary_configured() or settings.DEBUG:
            return
        
        try:
            if created and instance.image:
                public_id = f"items/item_{instance.item.pk}/image_{instance.pk}"
                
                result = upload_image_to_cloudinary(
                    instance.image.file,
                    folder="items",
                    public_id=public_id
                )
                
                if result:
                    logger.info(f"ItemImage {instance.pk} caricata su Cloudinary: {result['public_id']}")
                
        except Exception as e:
            logger.error(f"Errore signal handler ItemImage upload: {e}")
    
    
    @receiver(post_delete, sender=ItemImage)
    def handle_item_image_multiple_delete(sender, instance, **kwargs):
        """
        Elimina immagini multiple da Cloudinary
        """
        if not is_cloudinary_configured() or settings.DEBUG:
            return
        
        try:
            if instance.image:
                public_id = f"ninvendo/items/item_{instance.item.pk}/image_{instance.pk}"
                success = delete_cloudinary_image(public_id)
                
                if success:
                    logger.info(f"ItemImage {instance.pk} eliminata da Cloudinary")
                
        except Exception as e:
            logger.error(f"Errore signal handler ItemImage delete: {e}")


# Signal per ottimizzazione immagini esistenti
@receiver(pre_save, sender=Item)
def optimize_item_image_before_save(sender, instance, **kwargs):
    """
    Ottimizza immagini prima del salvataggio (solo per upload iniziali)
    """
    if not is_cloudinary_configured() or settings.DEBUG:
        return
    
    try:
        # Solo se è un nuovo oggetto o se l'immagine è cambiata
        if instance.pk is None:  # Nuovo oggetto
            if hasattr(instance, 'image') and instance.image:
                # Qui potresti aggiungere validazioni/ottimizzazioni pre-upload
                # Ad esempio, controllare dimensioni, formato, ecc.
                
                # Esempio: validazione dimensioni massime
                if hasattr(instance.image, 'file') and instance.image.file:
                    file_size = instance.image.file.size
                    max_size = getattr(settings, 'MAX_UPLOAD_SIZE', 10 * 1024 * 1024)  # 10MB
                    
                    if file_size > max_size:
                        raise ValueError(f"File troppo grande: {file_size/1024/1024:.1f}MB. Max: {max_size/1024/1024:.1f}MB")
                
                logger.debug(f"Pre-validazione immagine Item completata")
                
    except Exception as e:
        logger.error(f"Errore pre-save optimization: {e}")
        # Non bloccare il salvataggio per errori di ottimizzazione
        pass


def cleanup_orphaned_cloudinary_images():
    """
    Utility function per pulire immagini orfane su Cloudinary
    Può essere chiamata da un comando di gestione Django
    """
    if not is_cloudinary_configured():
        logger.warning("Cloudinary non configurato, cleanup saltato")
        return
    
    try:
        from .cloudinary_utils import get_folder_stats
        import cloudinary.api
        
        # Ottieni tutte le immagini dalla cartella ninvendo
        stats = get_folder_stats("ninvendo")
        
        if not stats:
            return
        
        orphaned_count = 0
        
        # Controlla ogni immagine se ha un corrispondente nel database
        for resource in stats['resources']:
            public_id = resource['public_id']
            
            # Estrai informazioni dal public_id
            if 'items/' in public_id:
                # Controlla se l'item esiste ancora
                try:
                    item_id = public_id.split('item_')[1].split('_')[0]
                    if not Item.objects.filter(pk=item_id).exists():
                        # Item non esiste più, elimina l'immagine
                        success = delete_cloudinary_image(public_id)
                        if success:
                            orphaned_count += 1
                            logger.info(f"Eliminata immagine orfana: {public_id}")
                except (IndexError, ValueError):
                    # Public ID non parsabile, salta
                    continue
            
            elif 'trade_messages/' in public_id:
                # Controlla se il messaggio esiste ancora
                try:
                    msg_id = public_id.split('msg_')[1]
                    if not TradeMessage.objects.filter(pk=msg_id).exists():
                        success = delete_cloudinary_image(public_id)
                        if success:
                            orphaned_count += 1
                            logger.info(f"Eliminata immagine messaggio orfana: {public_id}")
                except (IndexError, ValueError):
                    continue
        
        logger.info(f"Cleanup completato: {orphaned_count} immagini orfane eliminate")
        return orphaned_count
        
    except Exception as e:
        logger.error(f"Errore durante cleanup immagini orfane: {e}")
        return 0 signal handler Item image upload: {e}")


@receiver(post_delete, sender=Item)
def handle_item_image_delete(sender, instance, **kwargs):
    """
    Elimina immagine da Cloudinary quando viene eliminato un Item
    """
    if not is_cloudinary_configured():
        return
    
    if settings.DEBUG:
        return
    
    try:
        if hasattr(instance, 'image') and instance.image:
            # Estrai public_id dall'immagine
            if hasattr(instance.image, 'public_id'):
                public_id = instance.image.public_id
            else:
                # Ricostruisci public_id dal nome file
                public_id = f"ninvendo/items/item_{instance.pk}_{instance.slug}"
            
            success = delete_cloudinary_image(public_id)
            
            if success:
                logger.info(f"Immagine Item {instance.pk} eliminata da Cloudinary")
            else:
                logger.warning(f"Impossibile eliminare immagine Item {instance.pk} da Cloudinary")
                
    except Exception as e:
        logger.error(f"Errore
```


### project/cloudinary_utils.py

```python
"""
Utilities per gestire Cloudinary nel progetto NINVENDO
"""
import os
from django.conf import settings
from django.utils.html import format_html
from django.template.loader import render_to_string
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary import CloudinaryImage
import logging

logger = logging.getLogger(__name__)


def is_cloudinary_configured():
    """Verifica se Cloudinary è configurato correttamente"""
    try:
        cloud_name = getattr(settings, 'CLOUDINARY_STORAGE', {}).get('CLOUD_NAME')
        api_key = getattr(settings, 'CLOUDINARY_STORAGE', {}).get('API_KEY')
        api_secret = getattr(settings, 'CLOUDINARY_STORAGE', {}).get('API_SECRET')
        
        return all([cloud_name, api_key, api_secret]) and \
               cloud_name != 'your_cloud_name' and \
               api_key != 'your_api_key'
    except:
        return False


def get_cloudinary_url(image_field, transformation='medium'):
    """
    Genera URL Cloudinary per un'immagine con trasformazioni
    
    Args:
        image_field: Campo immagine del modello Django
        transformation: Nome della trasformazione (da settings.CLOUDINARY_TRANSFORMATIONS)
    
    Returns:
        str: URL dell'immagine trasformata
    """
    if not image_field:
        return None
        
    # Se non è configurato Cloudinary, usa URL normale
    if not is_cloudinary_configured():
        return image_field.url if hasattr(image_field, 'url') else None
    
    try:
        # Estrai public_id dal percorso
        if hasattr(image_field, 'public_id'):
            public_id = image_field.public_id
        elif hasattr(image_field, 'name'):
            # Per campi FileField, estrai il public_id dal name
            public_id = os.path.splitext(image_field.name)[0]
        else:
            return image_field.url if hasattr(image_field, 'url') else None
            
        # Ottieni parametri di trasformazione
        transform_params = settings.CLOUDINARY_TRANSFORMATIONS.get(
            transformation, 
            settings.CLOUDINARY_TRANSFORMATIONS['medium']
        )
        
        # Crea CloudinaryImage e genera URL
        cloudinary_image = CloudinaryImage(public_id)
        return cloudinary_image.build_url(**transform_params)
        
    except Exception as e:
        logger.warning(f"Errore generazione URL Cloudinary: {e}")
        return image_field.url if hasattr(image_field, 'url') else None


def get_optimized_image_tag(image_field, alt_text="", css_class="", transformation='medium'):
    """
    Genera tag HTML <img> ottimizzato con srcset per responsive images
    
    Args:
        image_field: Campo immagine
        alt_text: Testo alternativo
        css_class: Classi CSS
        transformation: Trasformazione base
    
    Returns:
        str: Tag HTML completo
    """
    if not image_field:
        return format_html(
            '<div class="no-image-placeholder {}">'
            '<span class="text-muted">📷 Nessuna immagine</span>'
            '</div>',
            css_class
        )
    
    try:
        base_url = get_cloudinary_url(image_field, transformation)
        if not base_url:
            # Fallback per sviluppo locale
            return format_html(
                '<img src="{}" alt="{}" class="{}" loading="lazy">',
                image_field.url, alt_text, css_class
            )
        
        # Se Cloudinary è configurato, crea srcset responsive
        if is_cloudinary_configured():
            # Genera diverse risoluzioni
            srcset_urls = []
            base_transform = settings.CLOUDINARY_TRANSFORMATIONS.get(transformation, {})
            base_width = base_transform.get('width', 400)
            
            # Crea varianti per diversi device pixel ratio
            for dpr in [1, 1.5, 2]:
                width = int(base_width * dpr)
                transform_params = base_transform.copy()
                transform_params['width'] = width
                transform_params['dpr'] = dpr
                
                if hasattr(image_field, 'public_id'):
                    public_id = image_field.public_id
                else:
                    public_id = os.path.splitext(image_field.name)[0]
                
                cloudinary_image = CloudinaryImage(public_id)
                url = cloudinary_image.build_url(**transform_params)
                srcset_urls.append(f"{url} {dpr}x")
            
            srcset = ", ".join(srcset_urls)
            
            return format_html(
                '<img src="{}" srcset="{}" alt="{}" class="{}" loading="lazy">',
                base_url, srcset, alt_text, css_class
            )
        else:
            return format_html(
                '<img src="{}" alt="{}" class="{}" loading="lazy">',
                base_url, alt_text, css_class
            )
            
    except Exception as e:
        logger.error(f"Errore generazione tag immagine: {e}")
        # Fallback sicuro
        return format_html(
            '<img src="{}" alt="{}" class="{}" loading="lazy">',
            image_field.url if hasattr(image_field, 'url') else '',
            alt_text, css_class
        )


def upload_image_to_cloudinary(image_file, folder="items", public_id=None):
    """
    Carica un'immagine su Cloudinary con ottimizzazioni
    
    Args:
        image_file: File immagine da caricare
        folder: Cartella di destinazione su Cloudinary
        public_id: ID pubblico personalizzato (opzionale)
    
    Returns:
        dict: Risultato upload Cloudinary
    """
    if not is_cloudinary_configured():
        logger.warning("Cloudinary non configurato, upload saltato")
        return None
    
    try:
        upload_options = {
            'folder': f"ninvendo/{folder}",
            'use_filename': True,
            'unique_filename': True if not public_id else False,
            'overwrite': False,
            'quality': 'auto:best',
            'format': 'auto',
            'flags': 'progressive',
            'transformation': [
                {'quality': 'auto:good'},
                {'fetch_format': 'auto'}
            ]
        }
        
        if public_id:
            upload_options['public_id'] = public_id
        
        result = cloudinary.uploader.upload(image_file, **upload_options)
        
        logger.info(f"Immagine caricata su Cloudinary: {result.get('public_id')}")
        return result
        
    except Exception as e:
        logger.error(f"Errore upload Cloudinary: {e}")
        return None


def delete_cloudinary_image(public_id):
    """
    Elimina un'immagine da Cloudinary
    
    Args:
        public_id: ID pubblico dell'immagine da eliminare
    
    Returns:
        bool: True se eliminata con successo
    """
    if not is_cloudinary_configured() or not public_id:
        return False
    
    try:
        result = cloudinary.uploader.destroy(public_id)
        success = result.get('result') == 'ok'
        
        if success:
            logger.info(f"Immagine eliminata da Cloudinary: {public_id}")
        else:
            logger.warning(f"Immagine non trovata su Cloudinary: {public_id}")
        
        return success
        
    except Exception as e:
        logger.error(f"Errore eliminazione Cloudinary: {e}")
        return False


def get_folder_stats(folder_path="ninvendo"):
    """
    Ottieni statistiche su una cartella Cloudinary
    
    Args:
        folder_path: Percorso della cartella
    
    Returns:
        dict: Statistiche della cartella
    """
    if not is_cloudinary_configured():
        return None
    
    try:
        # Ottieni informazioni sulla cartella
        result = cloudinary.api.resources(
            type="upload",
            prefix=folder_path,
            max_results=500
        )
        
        total_resources = result.get('total_count', 0)
        resources = result.get('resources', [])
        total_bytes = sum(r.get('bytes', 0) for r in resources)
        
        return {
            'total_images': total_resources,
            'total_size_mb': round(total_bytes / (1024 * 1024), 2),
            'resources': resources
        }
        
    except Exception as e:
        logger.error(f"Errore statistiche Cloudinary: {e}")
        return None


# Decorator per template tags
def cloudinary_templatetag(func):
    """Decorator per template tags che usano Cloudinary"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Errore template tag Cloudinary: {e}")
            return ""
    return wrapper
```


### project/context_processors.py

```python
"""
Context processors per NINVENDO
Rende disponibili le configurazioni del sito in tutti i template
"""

from django.conf import settings


def site_config(request):
    """
    Context processor per le configurazioni del sito
    Uso nei template: {{ SITE_NAME }}, {{ SITE_DESCRIPTION }}, etc.
    """
    return {
        'SITE_NAME': getattr(settings, 'SITE_NAME', 'NINVENDO'),
        'SITE_DESCRIPTION': getattr(settings, 'SITE_DESCRIPTION', 'A swap and market place for nintendo lovers'),
        'SITE_TAGLINE': getattr(settings, 'SITE_TAGLINE', 'Your Nintendo Gaming Community'),
        'SITE_URL': getattr(settings, 'SITE_URL', 'http://127.0.0.1:8000'),
    }


def cloudinary_context(request):
    """
    Aggiunge informazioni Cloudinary disponibili in tutti i template
    Uso nei template: {{ CLOUDINARY_CONFIGURED }}, {{ CLOUDINARY_ACTIVE }}, etc.
    """
    
    # Verifica se Cloudinary è configurato
    cloudinary_configured = (
        hasattr(settings, 'CLOUDINARY_STORAGE') and
        settings.CLOUDINARY_STORAGE.get('CLOUD_NAME', 'your_cloud_name') != 'your_cloud_name' and
        settings.CLOUDINARY_STORAGE.get('API_KEY', 'your_api_key') != 'your_api_key'
    )
    
    # Verifica se è attivo (basato su storage backend)
    cloudinary_active = (
        cloudinary_configured and 
        getattr(settings, 'DEFAULT_FILE_STORAGE', '').endswith('MediaCloudinaryStorage')
    )
    
    return {
        'CLOUDINARY_CONFIGURED': cloudinary_configured,
        'CLOUDINARY_ACTIVE': cloudinary_active,
        'CLOUDINARY_TRANSFORMATIONS': getattr(settings, 'CLOUDINARY_TRANSFORMATIONS', {}),
        'USE_CLOUDINARY_IN_DEV': getattr(settings, 'USE_CLOUDINARY_IN_DEV', False),
        'DEBUG': settings.DEBUG,
    }
```


### project/management/__init__.py

```python

```


### project/management/commands/__init__.py

```python

```


### project/management/commands/cloudinary_admin.py

```python
"""
Management command per amministrare Cloudinary
Uso: python manage.py cloudinary_admin [comando] [opzioni]
"""
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import transaction
import sys
import os

# Import delle utility Cloudinary
try:
    from project.cloudinary_utils import (
        is_cloudinary_configured,
        get_folder_stats,
        delete_cloudinary_image,
        upload_image_to_cloudinary
    )
    from project.cloudinary_signals import cleanup_orphaned_cloudinary_images
except ImportError as e:
    print(f"⚠️ Import error: {e}")
    # Fallback imports
    pass

from django_classified.models import Item
from trade.models import TradeMessage


class Command(BaseCommand):
    help = """
    Amministra Cloudinary per NINVENDO
    
    Comandi disponibili:
      status      - Mostra stato configurazione Cloudinary
      stats       - Statistiche utilizzo storage
      cleanup     - Rimuove immagini orfane
      migrate     - Migra immagini esistenti su Cloudinary
      test        - Testa configurazione con upload di prova
      backup      - Backup URLs immagini esistenti
    """
    
    def add_arguments(self, parser):
        parser.add_argument(
            'command',
            type=str,
            help='Comando da eseguire: status, stats, cleanup, migrate, test, backup'
        )
        
        parser.add_argument(
            '--force',
            action='store_true',
            help='Forza operazione senza conferma'
        )
        
        parser.add_argument(
            '--limit',
            type=int,
            default=100,
            help='Limite oggetti da processare (default: 100)'
        )
        
        parser.add_argument(
            '--folder',
            type=str,
            default='ninvendo',
            help='Cartella Cloudinary target (default: ninvendo)'
        )
        
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Simula operazione senza eseguirla'
        )
    
    def handle(self, *args, **options):
        command = options['command'].lower()
        
        # Dispatcher dei comandi
        command_map = {
            'status': self.handle_status,
            'stats': self.handle_stats,
            'cleanup': self.handle_cleanup,
            'migrate': self.handle_migrate,
            'test': self.handle_test,
            'backup': self.handle_backup,
        }
        
        if command not in command_map:
            raise CommandError(f"Comando non riconosciuto: {command}")
        
        try:
            command_map[command](options)
        except Exception as e:
            raise CommandError(f"Errore esecuzione comando '{command}': {e}")
    
    def handle_status(self, options):
        """Mostra stato configurazione Cloudinary"""
        self.stdout.write(self.style.HTTP_INFO("=== STATUS CLOUDINARY ==="))
        
        # Verifica configurazione
        configured = is_cloudinary_configured()
        status_icon = "✅" if configured else "❌"
        
        self.stdout.write(f"{status_icon} Configurazione: {'OK' if configured else 'MANCANTE'}")
        
        if configured:
            # Mostra dettagli configurazione (senza credenziali sensibili)
            cloudinary_settings = getattr(settings, 'CLOUDINARY_STORAGE', {})
            cloud_name = cloudinary_settings.get('CLOUD_NAME', 'N/A')
            
            self.stdout.write(f"🏷️  Cloud Name: {cloud_name}")
            self.stdout.write(f"🔐 API Key: {'***' + cloudinary_settings.get('API_KEY', '')[-4:] if cloudinary_settings.get('API_KEY') else 'N/A'}")
            self.stdout.write(f"🔧 Secure: {cloudinary_settings.get('SECURE', False)}")
            
            # Verifica storage backend
            storage_backend = getattr(settings, 'DEFAULT_FILE_STORAGE', 'N/A')
            self.stdout.write(f"💾 Storage Backend: {storage_backend}")
            
            # Debug mode
            debug_icon = "🛠️" if settings.DEBUG else "🚀"
            self.stdout.write(f"{debug_icon} Modalità: {'Sviluppo' if settings.DEBUG else 'Produzione'}")
            
        else:
            self.stdout.write(self.style.WARNING("⚠️  Cloudinary non configurato"))
            self.stdout.write("Imposta le variabili d'ambiente:")
            self.stdout.write("  CLOUDINARY_CLOUD_NAME=your_cloud_name")
            self.stdout.write("  CLOUDINARY_API_KEY=your_api_key") 
            self.stdout.write("  CLOUDINARY_API_SECRET=your_api_secret")
    
    def handle_stats(self, options):
        """Mostra statistiche utilizzo"""
        self.stdout.write(self.style.HTTP_INFO("=== STATISTICHE CLOUDINARY ==="))
        
        if not is_cloudinary_configured():
            self.stdout.write(self.style.ERROR("❌ Cloudinary non configurato"))
            return
        
        folder = options['folder']
        stats = get_folder_stats(folder)
        
        if not stats:
            self.stdout.write(self.style.WARNING("⚠️ Impossibile ottenere statistiche"))
            return
        
        self.stdout.write(f"📁 Cartella: {folder}")
        self.stdout.write(f"📷 Totale immagini: {stats['total_images']}")
        self.stdout.write(f"💾 Dimensione totale: {stats['total_size_mb']} MB")
        
        # Statistiche dettagliate per sottocartelle
        subcategories = {}
        for resource in stats['resources'][:20]:  # Primi 20 per non sovraccaricare
            public_id = resource['public_id']
            if '/' in public_id:
                category = public_id.split('/')[1] if public_id.count('/') > 1 else 'root'
                subcategories[category] = subcategories.get(category, 0) + 1
        
        if subcategories:
            self.stdout.write("\n📂 Breakdown per categoria:")
            for category, count in subcategories.items():
                self.stdout.write(f"  {category}: {count} immagini")
        
        # Conta immagini nel database locale
        items_with_images = Item.objects.exclude(image='').count()
        trade_messages_with_images = TradeMessage.objects.exclude(image='').count()
        
        self.stdout.write(f"\n🗃️  Database locale:")
        self.stdout.write(f"  Items con immagini: {items_with_images}")
        self.stdout.write(f"  Trade messages con immagini: {trade_messages_with_images}")
        
        total_db_images = items_with_images + trade_messages_with_images
        self.stdout.write(f"  Totale: {total_db_images}")
        
        # Differenza
        diff = stats['total_images'] - total_db_images
        if diff > 0:
            self.stdout.write(self.style.WARNING(f"⚠️ Possibili {diff} immagini orfane su Cloudinary"))
        elif diff < 0:
            self.stdout.write(self.style.WARNING(f"⚠️ {abs(diff)} immagini non migrate su Cloudinary"))
    
    def handle_cleanup(self, options):
        """Rimuove immagini orfane"""
        self.stdout.write(self.style.HTTP_INFO("=== CLEANUP IMMAGINI ORFANE ==="))
        
        if not is_cloudinary_configured():
            self.stdout.write(self.style.ERROR("❌ Cloudinary non configurato"))
            return
        
        if not options['force'] and not options['dry_run']:
            confirm = input("⚠️  Questa operazione eliminerà immagini da Cloudinary. Continuare? (y/N): ")
            if confirm.lower() != 'y':
                self.stdout.write("Operazione annullata.")
                return
        
        if options['dry_run']:
            self.stdout.write(self.style.WARNING("🧪 MODALITÀ DRY-RUN - Nessuna eliminazione effettuata"))
        
        # Esegui cleanup
        try:
            if options['dry_run']:
                # Simula cleanup (implementa versione dry-run se necessario)
                self.stdout.write("🔍 Analisi immagini orfane...")
                # TODO: Implementa logica dry-run
                orphaned_count = 0
            else:
                orphaned_count = cleanup_orphaned_cloudinary_images()
            
            if orphaned_count > 0:
                self.stdout.write(self.style.SUCCESS(f"✅ {orphaned_count} immagini orfane eliminate"))
            else:
                self.stdout.write("ℹ️  Nessuna immagine orfana trovata")
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Errore durante cleanup: {e}"))
    
    def handle_migrate(self, options):
        """Migra immagini esistenti su Cloudinary"""
        self.stdout.write(self.style.HTTP_INFO("=== MIGRAZIONE IMMAGINI ==="))
        
        if not is_cloudinary_configured():
            self.stdout.write(self.style.ERROR("❌ Cloudinary non configurato"))
            return
        
        limit = options['limit']
        dry_run = options['dry_run']
        
        if dry_run:
            self.stdout.write(self.style.WARNING("🧪 MODALITÀ DRY-RUN"))
        
        # Migra immagini Items
        self.stdout.write("🔄 Migrazione immagini Items...")
        items = Item.objects.exclude(image='')[:limit]
        
        migrated_items = 0
        for item in items:
            try:
                if not dry_run:
                    public_id = f"items/item_{item.pk}_{item.slug}"
                    result = upload_image_to_cloudinary(
                        item.image.file,
                        folder="items",
                        public_id=public_id
                    )
                    
                    if result:
                        migrated_items += 1
                        self.stdout.write(f"  ✅ Item {item.pk}: {item.title[:30]}...")
                    else:
                        self.stdout.write(f"  ❌ Errore Item {item.pk}")
                else:
                    migrated_items += 1
                    self.stdout.write(f"  🧪 Item {item.pk}: {item.title[:30]}... (simulato)")
                    
            except Exception as e:
                self.stdout.write(f"  ❌ Errore Item {item.pk}: {e}")
        
        # Migra immagini TradeMessage
        self.stdout.write("🔄 Migrazione immagini Trade Messages...")
        trade_messages = TradeMessage.objects.exclude(image='')[:limit]
        
        migrated_messages = 0
        for msg in trade_messages:
            try:
                if not dry_run:
                    public_id = f"trade_messages/trade_{msg.trade.pk}/msg_{msg.pk}"
                    result = upload_image_to_cloudinary(
                        msg.image.file,
                        folder="trade_messages",
                        public_id=public_id
                    )
                    
                    if result:
                        migrated_messages += 1
                        self.stdout.write(f"  ✅ Message {msg.pk}")
                    else:
                        self.stdout.write(f"  ❌ Errore Message {msg.pk}")
                else:
                    migrated_messages += 1
                    self.stdout.write(f"  🧪 Message {msg.pk} (simulato)")
                    
            except Exception as e:
                self.stdout.write(f"  ❌ Errore Message {msg.pk}: {e}")
        
        # Riepilogo
        total_migrated = migrated_items + migrated_messages
        self.stdout.write(self.style.SUCCESS(f"\n✅ Migrazione completata:"))
        self.stdout.write(f"  📦 Items: {migrated_items}")
        self.stdout.write(f"  💬 Messages: {migrated_messages}")
        self.stdout.write(f"  📊 Totale: {total_migrated}")
    
    def handle_test(self, options):
        """Testa configurazione Cloudinary"""
        self.stdout.write(self.style.HTTP_INFO("=== TEST CLOUDINARY ==="))
        
        if not is_cloudinary_configured():
            self.stdout.write(self.style.ERROR("❌ Cloudinary non configurato"))
            return
        
        try:
            # Test connessione API
            import cloudinary.api

<<TRUNCATED FILE: limited to 300 lines>>
```


### project/settings.py

```python
# -*- coding:utf-8 -*-
import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(
    DEBUG=(bool, False),
    CACHE_URL=(str, 'locmemcache://'),
    EMAIL_URL=(str, 'consolemail://'),
    SECRET_KEY=(str, 'secret'),
    DATABASE_URL=(str, 'sqlite:///db.sqlite'),
)

env.read_env(str(os.path.join(BASE_DIR, ".env")))

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')

ADMINS = (
    ('Demo Classified Admin', os.environ.get('ADMIN_EMAIL', '***REDACTED***')),
)

MANAGERS = ADMINS

# Expected comma separated string with the ALLOWED_HOSTS list
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '***REDACTED***').split(',')

# (Opzionale ma utile in deploy dietro proxy/Render per OAuth)
# Comma-separated, es: "https://nintendo-swap.onrender.com"
CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', '***REDACTED***') if os.environ.get('CSRF_TRUSTED_ORIGINS') else []

DATABASES = {
    'default': env.db(),
}

# Cache configuration for development
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'default-cache',
        'OPTIONS': {
            'MAX_ENTRIES': 1000,
            'CULL_FREQUENCY': 3,
        }
    }
}

# Local time zone for this installation.
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ============================================
# CONFIGURAZIONE CLOUDINARY PER IMMAGINI
# ============================================

# Configurazione Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUDINARY_CLOUD_NAME', default='your_cloud_name'),
    'API_KEY': env('CLOUDINARY_API_KEY', default='your_api_key'), 
    'API_SECRET': env('CLOUDINARY_API_SECRET', default='your_api_secret'),
    'SECURE': True,  # Usa HTTPS
}

# Solo se Cloudinary è configurato correttamente
if (CLOUDINARY_STORAGE['CLOUD_NAME'] != 'your_cloud_name' and 
    CLOUDINARY_STORAGE['API_KEY'] != 'your_api_key'):
    
    import cloudinary
    import cloudinary.uploader
    import cloudinary.api
    
    cloudinary.config(
        cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
        api_key=CLOUDINARY_STORAGE['API_KEY'],
        api_secret=CLOUDINARY_STORAGE['API_SECRET'],
        secure=CLOUDINARY_STORAGE['SECURE']
    )
    
    # Configurazioni Cloudinary avanzate
    CLOUDINARY_STORAGE.update({
        'FOLDER': 'ninvendo',  # Cartella principale
        'FORMAT': 'auto',      # Formato automatico (WebP quando possibile)
        'QUALITY': 'auto:best',  # Qualità automatica ottimizzata
        'FETCH_FORMAT': 'auto', # Formato di fetch automatico
        'FLAGS': 'progressive', # Caricamento progressivo
    })

# ============================================
# CONFIGURAZIONI CLOUDINARY TRASFORMAZIONI
# ============================================

# Preset di trasformazioni per diverse dimensioni
CLOUDINARY_TRANSFORMATIONS = {
    'thumbnail': {
        'width': 150,
        'height': 150,
        'crop': 'fill',
        'quality': 'auto:good',
        'format': 'auto'
    },
    'medium': {
        'width': 400, 
        'height': 300,
        'crop': 'fill',
        'quality': 'auto:good',
        'format': 'auto'
    },
    'large': {
        'width': 800,
        'height': 600,
        'crop': 'fit',
        'quality': 'auto:best',
        'format': 'auto'
    },
    'trade_message': {
        'width': 300,
        'height': 300,
        'crop': 'fit',
        'quality': 'auto:good',
        'format': 'auto'
    },
    'hero': {
        'width': 1200,
        'height': 400,
        'crop': 'fill',
        'quality': 'auto:best',
        'format': 'auto'
    }
}

# ============================================
# MEDIA E STATIC FILES
# ============================================

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like '/home/html/static' or 'C:/www/django/static'.
)

# Configurazioni upload immagini
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10MB max per immagine
ALLOWED_IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.webp']

# Configurazione Storage - MANTENIAMO LA LOGICA ORIGINALE
# Usa Cloudinary per i MEDIA (file caricati dagli utenti) SOLO SE CONFIGURATO
if not DEBUG and (CLOUDINARY_STORAGE['CLOUD_NAME'] != 'your_cloud_name'):
    # PRODUZIONE: Cloudinary per media files se configurato
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
else:
    # SVILUPPO O CLOUDINARY NON CONFIGURATO: Filesystem locale
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

STORAGES = {
    "default": {
        "BACKEND": DEFAULT_FILE_STORAGE,
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MIDDLEWARE = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# 🔐 Backends: Google OAuth2 + username/password Django (e manteniamo Facebook se già configurato)
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',     # Google Login
    'social_core.backends.facebook.FacebookOAuth2', # (opzionale) Facebook già presente
    'django.contrib.auth.backends.ModelBackend',    # Username/Password nativo Django
)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Social Auth context processors
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

                # Django Classified context processors
                'django_classified.context_processors.common_values',
                
                # ⭐ CLOUDINARY CONTEXT PROCESSOR (se necessario)
                'project.context_processors.site_config',
                'project.templatetags.cloudinary_tags.cloudinary_context',
            ],
            'debug': True
        },
    },
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',  # ⭐ AGGIUNTO - era mancante!

    'bootstrapform',
    'sorl.thumbnail',
    'django_classified',
    'social_django',

    # ⭐ MODULI ESSENZIALI PER BARATTO
    'crispy_forms',         # django-crispy-forms
    'crispy_bootstrap4',    # crispy bootstrap4 template pack
    'widget_tweaks',        # django-widget-tweaks
    'django_extensions',    # utilities per sviluppo

    # ⭐ CLOUDINARY SUPPORT - ORDINE CORRETTO
    'cloudinary_storage',   # DEVE essere prima di cloudinary
    'cloudinary',          # cloudinary

    'demo',
    'registration',  
    "trade",
    'payments',
    
    # ⭐ PROJECT APP (per management commands e utilities) - SE NECESSARIO
    'project',
]

# ⭐ CONFIGURAZIONI CRISPY FORMS
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Email per notifiche (già presente, assicuriamoci sia configurato)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # development
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # production

ACCOUNT_ACTIVATION_DAYS = 7  # per backend 'default' (con email)

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/'

DCF_SITE_NAME = 'NinVendo : a place for NinTendo lovers'

# ---- Social Auth: Google (aggiunto) ----
# Imposta questi valori nell'ambiente (.env o Render env)
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '***REDACTED***'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '***REDACTED***'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

# Se sei dietro proxy/https terminato a monte (es. Render), abilita il redirect HTTPS:
# In locale lascialo False; in produzione metti env SOCIAL_AUTH_REDIRECT_IS_HTTPS='***REDACTED***'
SOCIAL_AUTH_REDIRECT_IS_HTTPS = '***REDACTED***'SOCIAL_AUTH_REDIRECT_IS_HTTPS', default=False)

# ---- Social Auth: Facebook (già presente, opzionale) ----
SOCIAL_AUTH_FACEBOOK_KEY = '***REDACTED***'SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = '***REDACTED***'SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = '***REDACTED***'email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = '***REDACTED***'
    'fields': 'id, name, email'
}

SOCIAL_AUTH_EMAIL_FORM_HTML = '***REDACTED***'  # ⭐ MANTENUTO ORIGINALE
SOCIAL_AUTH_EMAIL_VALIDATION_URL = '***REDACTED***'

SOCIAL_AUTH_PIPELINE = '***REDACTED***'
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.mail.mail_validation',
    'social_core.pipeline.user.create_user',

<<TRUNCATED FILE: limited to 300 lines>>
```


### project/templatetags/cloudinary_tags.py

```python
"""
Template tags per integrare Cloudinary nei template Django
"""
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from ..cloudinary_utils import (
    get_cloudinary_url,
    get_optimized_image_tag,
    is_cloudinary_configured,
    cloudinary_templatetag
)
import logging

register = template.Library()
logger = logging.getLogger(__name__)


@register.simple_tag
@cloudinary_templatetag
def cloudinary_url(image_field, transformation='medium'):
    """
    Genera URL Cloudinary per un'immagine
    
    Uso: {% cloudinary_url item.image 'thumbnail' %}
    """
    return get_cloudinary_url(image_field, transformation) or ''


@register.simple_tag
@cloudinary_templatetag
def cloudinary_img(image_field, alt_text="", css_class="img-fluid", transformation='medium'):
    """
    Genera tag <img> ottimizzato con Cloudinary
    
    Uso: {% cloudinary_img item.image "Descrizione" "img-fluid rounded" "large" %}
    """
    html = get_optimized_image_tag(image_field, alt_text, css_class, transformation)
    return mark_safe(html)


@register.simple_tag
@cloudinary_templatetag 
def cloudinary_thumbnail(image_field, alt_text="", css_class="thumbnail"):
    """
    Genera thumbnail ottimizzata
    
    Uso: {% cloudinary_thumbnail item.image "Thumbnail prodotto" %}
    """
    html = get_optimized_image_tag(image_field, alt_text, css_class, 'thumbnail')
    return mark_safe(html)


@register.simple_tag
@cloudinary_templatetag
def cloudinary_responsive_img(image_field, alt_text="", css_class="img-responsive", sizes="(max-width: 768px) 100vw, 50vw"):
    """
    Genera immagine completamente responsive con sizes attribute
    
    Uso: {% cloudinary_responsive_img item.image "Prodotto" "img-fluid" "(max-width: 768px) 100vw, 50vw" %}
    """
    if not image_field:
        return mark_safe(f'<div class="no-image-placeholder {css_class}"><span class="text-muted">📷 Nessuna immagine</span></div>')
    
    try:
        # URL base
        base_url = get_cloudinary_url(image_field, 'medium')
        if not base_url:
            return mark_safe(f'<img src="{image_field.url}" alt="{alt_text}" class="{css_class}" loading="lazy">')
        
        # Se Cloudinary configurato, crea srcset completo per responsive
        if is_cloudinary_configured():
            # Diverse larghezze per responsive breakpoints
            widths = [320, 480, 640, 800, 1024, 1200]
            srcset_urls = []
            
            for width in widths:
                # Usa l'utility per generare URL con larghezza specifica
                from cloudinary import CloudinaryImage
                import os
                
                if hasattr(image_field, 'public_id'):
                    public_id = image_field.public_id
                else:
                    public_id = os.path.splitext(image_field.name)[0]
                
                cloudinary_image = CloudinaryImage(public_id)
                url = cloudinary_image.build_url(
                    width=width,
                    crop='scale',
                    quality='auto:good',
                    format='auto'
                )
                srcset_urls.append(f"{url} {width}w")
            
            srcset = ", ".join(srcset_urls)
            
            return mark_safe(format_html(
                '<img src="{}" srcset="{}" sizes="{}" alt="{}" class="{}" loading="lazy">',
                base_url, srcset, sizes, alt_text, css_class
            ))
        else:
            return mark_safe(format_html(
                '<img src="{}" alt="{}" class="{}" loading="lazy">',
                base_url, alt_text, css_class
            ))
            
    except Exception as e:
        logger.error(f"Errore cloudinary_responsive_img: {e}")
        return mark_safe(f'<img src="{image_field.url}" alt="{alt_text}" class="{css_class}" loading="lazy">')


@register.inclusion_tag('cloudinary/image_gallery.html')
@cloudinary_templatetag
def cloudinary_gallery(images, thumbnail_class="col-md-3", lightbox=True):
    """
    Crea una galleria di immagini con Cloudinary
    
    Uso: {% cloudinary_gallery item.images.all %}
    """
    return {
        'images': images,
        'thumbnail_class': thumbnail_class,
        'lightbox': lightbox,
        'cloudinary_configured': is_cloudinary_configured()
    }


@register.simple_tag
def cloudinary_status():
    """
    Verifica stato configurazione Cloudinary
    
    Uso: {% cloudinary_status %}
    """
    return "✅ Configurato" if is_cloudinary_configured() else "❌ Non configurato"


@register.filter
@cloudinary_templatetag
def cloudinary_transform(image_field, transformation):
    """
    Filter per trasformazioni Cloudinary
    
    Uso: {{ item.image|cloudinary_transform:"thumbnail" }}
    """
    return get_cloudinary_url(image_field, transformation) or ''


@register.simple_tag
@cloudinary_templatetag
def cloudinary_background_img(image_field, css_class="hero-bg", transformation='large'):
    """
    Genera CSS per background-image con Cloudinary
    
    Uso: {% cloudinary_background_img hero.image "hero-section" "large" %}
    """
    if not image_field:
        return mark_safe(f'<div class="{css_class} no-bg-image"></div>')
    
    url = get_cloudinary_url(image_field, transformation)
    if not url:
        url = image_field.url
    
    style = f'background-image: url({url}); background-size: cover; background-position: center;'
    
    return mark_safe(format_html(
        '<div class="{}" style="{}"></div>',
        css_class, style
    ))


@register.simple_tag(takes_context=True)
@cloudinary_templatetag  
def cloudinary_share_image(context, image_field, transformation='large'):
    """
    Genera URL assoluto per condivisione social (Open Graph)
    
    Uso: {% cloudinary_share_image item.image "large" %}
    """
    if not image_field:
        return ""
    
    url = get_cloudinary_url(image_field, transformation)
    if not url:
        url = image_field.url
    
    # Converti in URL assoluto se necessario
    request = context.get('request')
    if request and not url.startswith('http'):
        url = request.build_absolute_uri(url)
    
    return url


# Template context processor
def cloudinary_context(request):
    """
    Context processor per aggiungere info Cloudinary in tutti i template
    """
    return {
        'CLOUDINARY_CONFIGURED': is_cloudinary_configured(),
        'CLOUDINARY_TRANSFORMATIONS': getattr(settings, 'CLOUDINARY_TRANSFORMATIONS', {})
    }
```


### project/urls.py

```python
from django.urls import include, re_path, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    re_path('', include('django_classified.urls', namespace='django_classified')),
    re_path('social/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),

    # Auth base
    path('login/', auth_views.LoginView.as_view(template_name='django_classified/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # Password reset (flow completo)
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='django_classified/password_reset_form.html',
        email_template_name='django_classified/password_reset_email.txt',
        subject_template_name='django_classified/password_reset_subject.txt',
        success_url='/password-reset/done/'
    ), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='django_classified/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='django_classified/password_reset_confirm.html',
        success_url='/reset/done/'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='django_classified/password_reset_complete.html'
    ), name='password_reset_complete'),

    # Pagina usata da social auth (se serve)
    path('email-sent/', TemplateView.as_view(template_name='django_classified/email_sent.html'), name='email_sent'),

    # Registrazione utenti (django-registration-redux, backend simple)
    path('accounts/', include('registration.backends.simple.urls')),

    # Modulo "baratto"
    path('trade/', include('trade.urls', namespace='trade')),

    # ⭐ NUOVO MODULO PAGAMENTI
    path('payments/', include('payments.urls', namespace='payments')),  # <-- Aggiungi questa riga

    # Debug Cloudinary (solo in sviluppo)
    path('debug/cloudinary/', TemplateView.as_view(template_name='debug_cloudinary.html'), name='debug_cloudinary'),

   

    path('debug/cloudinary/', TemplateView.as_view(template_name='debug_simple.html'), name='debug_cloudinary'),
]



# Alla fine del file
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```


### README_CLOUDINARY.md

```md
# 📷 Cloudinary Integration - NINVENDO

Guida completa per configurare e utilizzare Cloudinary per la gestione delle immagini nel progetto NINVENDO.

## 🚀 Panoramica

Cloudinary è un servizio cloud per la gestione, ottimizzazione e distribuzione di immagini. Offre:

- **🔄 Ottimizzazione automatica** - Ridimensionamento, compressione, formato automatico
- **🌍 CDN globale** - Distribuzione veloce in tutto il mondo  
- **📱 Immagini responsive** - Adattamento automatico ai diversi device
- **🎨 Trasformazioni on-the-fly** - Ritaglio, filtri, effetti in tempo reale
- **💾 Storage sicuro** - Backup e ridondanza automatici

## 🛠️ Setup Cloudinary

### 1. Registrazione Account

1. Vai su [cloudinary.com](https://cloudinary.com)
2. Registra un account gratuito (25GB storage + 25GB traffico/mese)
3. Accedi al **Dashboard**

### 2. Ottenere le Credenziali

Dal dashboard Cloudinary copia:

```bash
Cloud Name: your_cloud_name
API Key: 123456789012345  
API Secret: your_api_secret
```

### 3. Configurazione Ambiente

Aggiungi al tuo file `.env`:

```bash
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 4. Verifica Configurazione

```bash
python manage.py cloudinary_admin status
```

## 📋 Funzionalità Implementate

### 🎯 Template Tags

#### Immagine Ottimizzata Base
```html
{% load cloudinary_tags %}

<!-- Immagine responsive ottimizzata -->
{% cloudinary_img item.image "Descrizione" "img-fluid" "medium" %}
```

#### URL Cloudinary
```html
<!-- Solo URL per uso in CSS/JS -->
{% cloudinary_url item.image "large" %}
```

#### Thumbnail
```html
<!-- Thumbnail 150x150 -->
{% cloudinary_thumbnail item.image "Prodotto" "thumbnail-class" %}
```

#### Immagine Responsive Completa
```html
<!-- Con srcset per tutti i breakpoints -->
{% cloudinary_responsive_img item.image "Prodotto" "img-fluid" "(max-width: 768px) 100vw, 50vw" %}
```

#### Galleria Immagini
```html
<!-- Galleria con lightbox -->
{% cloudinary_gallery item.images.all "col-md-3" True %}
```

#### Background Image CSS
```html
<!-- Div con background-image ottimizzata -->
{% cloudinary_background_img hero.image "hero-section" "large" %}
```

### 🔧 Trasformazioni Predefinite

Configurate in `settings.py`:

```python
CLOUDINARY_TRANSFORMATIONS = {
    'thumbnail': {    # 150x150, ritagliata
        'width': 150,
        'height': 150,
        'crop': 'fill',
        'quality': 'auto:good',
        'format': 'auto'
    },
    'medium': {       # 400x300, adattata
        'width': 400,
        'height': 300, 
        'crop': 'fill',
        'quality': 'auto:good',
        'format': 'auto'
    },
    'large': {        # 800x600, preserva proporzioni
        'width': 800,
        'height': 600,
        'crop': 'fit',
        'quality': 'auto:best',
        'format': 'auto'
    }
}
```

### 🤖 Upload Automatico

Gli upload su Cloudinary avvengono automaticamente tramite **Django signals**:

- **Nuovi Item** → Upload immagine principale
- **Nuovi TradeMessage** → Upload immagine allegata
- **Eliminazione** → Cleanup automatico su Cloudinary

## 🎛️ Management Commands

### Status e Diagnostica

```bash
# Verifica configurazione
python manage.py cloudinary_admin status

# Statistiche utilizzo storage  
python manage.py cloudinary_admin stats

# Test connessione e upload
python manage.py cloudinary_admin test
```

### Migrazione Immagini

```bash
# Migra immagini esistenti su Cloudinary
python manage.py cloudinary_admin migrate --limit 100

# Simulazione senza upload reale
python manage.py cloudinary_admin migrate --dry-run --limit 10
```

### Pulizia Storage

```bash
# Rimuovi immagini orfane da Cloudinary
python manage.py cloudinary_admin cleanup

# Simulazione pulizia
python manage.py cloudinary_admin cleanup --dry-run

# Backup URL prima della pulizia
python manage.py cloudinary_admin backup
```

## 🏗️ Architettura del Sistema

### Flusso Upload

1. **Utente carica immagine** → Salvata localmente (sviluppo) o Cloudinary (produzione)
2. **Signal handler** → Upload automatico su Cloudinary (solo produzione)
3. **Template rendering** → URL ottimizzati tramite template tags
4. **Browser** → Carica immagini ottimizzate da CDN Cloudinary

### Storage Strategy

- **🛠️ Sviluppo**: Filesystem locale + template tags simulano Cloudinary
- **🚀 Produzione**: Upload diretto su Cloudinary + CDN delivery

### File Organization

```
ninvendo/                    # Cartella root su Cloudinary
├── items/                   # Immagini prodotti
│   ├── item_1_nintendo-switch/
│   └── item_2_pokemon-cards/
├── trade_messages/          # Immagini messaggi scambi
│   ├── trade_1/msg_1/
│   └── trade_1/msg_2/
└── test/                   # Immagini di test
```

## 🎨 Esempi Pratici

### Lista Prodotti con Thumbnail

```html
{% load cloudinary_tags %}

<div class="products-grid">
    {% for item in items %}
        <div class="product-card">
            <!-- Thumbnail ottimizzata 150x150 -->
            {% cloudinary_thumbnail item.image item.title "product-thumb" %}
            
            <h5>{{ item.title }}</h5>
            <p class="price">{{ item.price }}€</p>
        </div>
    {% endfor %}
</div>
```

### Dettaglio Prodotto Responsive

```html
{% load cloudinary_tags %}

<div class="product-detail">
    <!-- Immagine principale responsive -->
    <div class="main-image">
        {% cloudinary_responsive_img item.image item.title "img-fluid" "(max-width: 768px) 100vw, 60vw" %}
    </div>
    
    <!-- Galleria immagini aggiuntive -->
    {% if item.images.all %}
        <div class="image-gallery">
            {% cloudinary_gallery item.images.all "col-md-3" True %}
        </div>
    {% endif %}
</div>
```

### Meta Tag Open Graph

```html
{% load cloudinary_tags %}

<!-- Per condivisione social media -->
<meta property="og:image" content="{% cloudinary_share_image item.image 'large' %}" />
```

### Hero Section con Background

```html
{% load cloudinary_tags %}

<!-- Hero con background ottimizzata -->
{% cloudinary_background_img hero.image "hero-banner d-flex align-items-center justify-content-center" "hero" %}
    <div class="hero-content text-white text-center">
        <h1>Benvenuto su NINVENDO</h1>
        <p>Il marketplace per i fan di Nintendo</p>
    </div>
</div>

<style>
.hero-banner {
    min-height: 60vh;
    background-size: cover;
    background-position: center;
    position: relative;
}

.hero-banner::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0; 
    bottom: 0;
    background: rgba(0,0,0,0.4);
    z-index: 1;
}

.hero-content {
    position: relative;
    z-index: 2;
}
</style>
```

## 🔍 Debug e Troubleshooting

### Verifiche Comuni

```bash
# 1. Configurazione
python manage.py cloudinary_admin status

# 2. Test upload
python manage.py cloudinary_admin test

# 3. Verifica immagini nel database
python manage.py shell
>>> from django_classified.models import Item
>>> Item.objects.filter(image__isnull=False).count()
```

### Log di Debug


<<TRUNCATED FILE: limited to 300 lines>>
```


### requirements.txt

```

boto3==1.35.92 
django-classified==1.1.1
django-environ==0.11.2
django==5.1.8
gunicorn==23.0.0
psycopg2-binary==2.9.10
python-memcached==1.62
social-auth-app-django==5.4.2
whitenoise==6.8.2
django-fsm==3.0.0


django-crispy-forms==2.1
crispy-bootstrap4==2024.1
django-widget-tweaks==1.5.0
django-extensions==3.2.3


django-notifications-hq==1.8.0  

stripe==7.0.0

# ============================================
# CLOUDINARY SUPPORT - AGGIUNTO
# ============================================
cloudinary==1.40.0
django-cloudinary-storage==0.3.0
pillow==10.4.0
```


### templates/cloudinary/image_gallery.html

```html
{% load cloudinary_tags %}

<div class="cloudinary-gallery">
    <div class="row">
        {% for image in images %}
            <div class="{{ thumbnail_class }} mb-3">
                <div class="image-container position-relative">
                    {% if lightbox %}
                        <a href="{% cloudinary_url image 'large' %}" 
                           data-lightbox="gallery" 
                           data-title="Immagine {{ forloop.counter }}">
                            {% cloudinary_img image "Immagine prodotto" "img-fluid rounded shadow-sm" "medium" %}
                        </a>
                    {% else %}
                        {% cloudinary_img image "Immagine prodotto" "img-fluid rounded shadow-sm" "medium" %}
                    {% endif %}
                    
                    <!-- Overlay info se necessario -->
                    <div class="image-overlay position-absolute" style="bottom: 5px; right: 5px;">
                        <span class="badge badge-dark">{{ forloop.counter }}/{{ images.count }}</span>
                    </div>
                </div>
            </div>
        {% empty %}
            <div class="col-12 text-center">
                <div class="no-images-placeholder p-4 bg-light rounded">
                    <i class="fas fa-images fa-3x text-muted mb-2"></i>
                    <p class="text-muted mb-0">Nessuna immagine disponibile</p>
                </div>
            </div>
        {% endfor %}
    </div>
</div>

{% if lightbox and images %}
    <!-- Includi Lightbox CSS/JS se non già presente -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/js/lightbox.min.js"></script>
    
    <script>
        // Configurazione Lightbox
        lightbox.option({
            'resizeDuration': 200,
            'wrapAround': true,
            'fadeDuration': 300
        });
    </script>
{% endif %}

<style>
    .cloudinary-gallery .image-container {
        overflow: hidden;
        border-radius: 0.5rem;
        transition: transform 0.3s ease;
    }
    
    .cloudinary-gallery .image-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .no-images-placeholder {
        border: 2px dashed #dee2e6;
    }
    
    .image-overlay {
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .image-container:hover .image-overlay {
        opacity: 1;
    }
</style>
```


### templates/debug_cloudinary.html

```html
{% extends "django_classified/_base.html" %}
{% load cloudinary %}

{% block title %}🔧 Debug Cloudinary - {{ SITE_NAME }}{% endblock %}

{% block body %}
<div class="container mt-4">
    <h1>🔧 Debug Cloudinary</h1>
    
    <!-- Info Sito -->
    <div class="card mb-4">
        <div class="card-header bg-info text-white">
            <h5>🏠 Configurazione Sito</h5>
        </div>
        <div class="card-body">
            <p><strong>Nome:</strong> {{ SITE_NAME }}</p>
            <p><strong>Descrizione:</strong> {{ SITE_DESCRIPTION }}</p>
            <p><strong>Tagline:</strong> {{ SITE_TAGLINE }}</p>
            <p><strong>URL:</strong> {{ SITE_URL }}</p>
            <p><strong>Debug Mode:</strong> {{ DEBUG|yesno:"✅ Attivo,❌ Disattivo" }}</p>
        </div>
    </div>

    <!-- Status Cloudinary -->
    <div class="card mb-4">
        <div class="card-header bg-primary text-white">
            <h5>☁️ Status Cloudinary</h5>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-md-6">
                    <p><strong>Configurato:</strong> 
                        <span class="badge badge-{{ CLOUDINARY_CONFIGURED|yesno:'success,danger' }}">
                            {{ CLOUDINARY_CONFIGURED|yesno:"✅ SI,❌ NO" }}
                        </span>
                    </p>
                    <p><strong>Attivo:</strong> 
                        <span class="badge badge-{{ CLOUDINARY_ACTIVE|yesno:'success,warning' }}">
                            {{ CLOUDINARY_ACTIVE|yesno:"🌥️ Cloudinary,📁 Filesystem" }}
                        </span>
                    </p>
                    <p><strong>Dev Mode:</strong> 
                        <span class="badge badge-{{ USE_CLOUDINARY_IN_DEV|yesno:'info,secondary' }}">
                            {{ USE_CLOUDINARY_IN_DEV|yesno:"🧪 Test Mode,📁 Locale" }}
                        </span>
                    </p>
                </div>
                <div class="col-md-6">
                    {% if CLOUDINARY_TRANSFORMATIONS %}
                        <p><strong>Trasformazioni:</strong></p>
                        <ul class="small">
                            {% for name, config in CLOUDINARY_TRANSFORMATIONS.items %}
                                <li>{{ name }}: {{ config.width }}x{{ config.height }}</li>
                            {% endfor %}
                        </ul>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>

    <!-- Test Template Tags -->
    {% if CLOUDINARY_CONFIGURED %}
        <div class="card mb-4">
            <div class="card-header bg-success text-white">
                <h5>🏷️ Test Template Tags</h5>
            </div>
            <div class="card-body">
                <p>I template tags Cloudinary sono disponibili:</p>
                <ul>
                    <li>✅ <code>{% templatetag openblock %} load cloudinary_tags {% templatetag closeblock %}</code></li>
                    <li>✅ <code>{% templatetag openblock %} cloudinary_img item.image {% templatetag closeblock %}</code></li>
                    <li>✅ <code>{% templatetag openblock %} cloudinary_url item.image 'medium' {% templatetag closeblock %}</code></li>
                </ul>
                
                <!-- Test immagine se disponibile -->
                {% comment %}
                Se hai un'immagine di test puoi decommentare:
                {% if test_item.image %}
                    <div class="mt-3">
                        <h6>Esempio Immagine:</h6>
                        {% cloudinary_img test_item.image "Test image" "img-fluid" "medium" %}
                    </div>
                {% endif %}
                {% endcomment %}
            </div>
        </div>
    {% else %}
        <div class="card mb-4">
            <div class="card-header bg-warning text-white">
                <h5>⚠️ Cloudinary Non Configurato</h5>
            </div>
            <div class="card-body">
                <p>Per attivare Cloudinary:</p>
                <ol>
                    <li>Configura le variabili d'ambiente nel <code>.env</code>:
                        <pre class="bg-light p-2 mt-2">
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
USE_CLOUDINARY_IN_DEV=True</pre>
                    </li>
                    <li>Riavvia il server: <code>python manage.py runserver</code></li>
                    <li>Testa: <code>python manage.py cloudinary_admin status</code></li>
                </ol>
            </div>
        </div>
    {% endif %}

    <!-- Comandi Utili -->
    <div class="card mb-4">
        <div class="card-header bg-dark text-white">
            <h5>🛠️ Comandi Utili</h5>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-md-6">
                    <h6>Verifica:</h6>
                    <pre class="bg-light p-2 small">python manage.py cloudinary_admin status</pre>
                    
                    <h6>Test:</h6>
                    <pre class="bg-light p-2 small">python manage.py cloudinary_admin test</pre>
                </div>
                <div class="col-md-6">
                    <h6>Migrazione:</h6>
                    <pre class="bg-light p-2 small">python manage.py cloudinary_admin migrate --limit 10</pre>
                    
                    <h6>Statistiche:</h6>
                    <pre class="bg-light p-2 small">python manage.py cloudinary_admin stats</pre>
                </div>
            </div>
        </div>
    </div>

    <!-- Link Utili -->
    <div class="text-center">
        <a href="/" class="btn btn-primary">🏠 Torna alla Home</a>
        <a href="/admin/" class="btn btn-secondary">🔧 Admin</a>
        {% if user.is_staff %}
            <a href="{% url 'django_classified:item-new' %}" class="btn btn-success">➕ Testa Upload Immagine</a>
        {% endif %}
    </div>
</div>

<style>
    pre {
        font-size: 0.9em;
        border-radius: 4px;
    }
    
    .badge {
        font-size: 0.9em;
    }
    
    .card-header h5 {
        margin-bottom: 0;
    }
</style>
{% endblock %}
```


### templates/django_classified/item_detail.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n %}
{% comment %}⭐ CARICA CLOUDINARY TAGS SE DISPONIBILI{% endcomment %}
{% load cloudinary_tags %}

{% block title %}{{ item.title }} - {{ item.price }}€{% endblock %}

{% block meta_keywords %}{{ item.title }}, {{ item.area.title }}, {{ item.category.title }}, {{ item.group.title }}{% endblock meta_keywords %}

{% block meta_og %}
    <meta property="og:title" content="{{ item.title }}" />
    <meta property="og:description" content="{{ item.description|truncatewords:30|striptags }}" />
    {% comment %}⭐ USA CLOUDINARY PER IMMAGINI SOCIAL SE DISPONIBILE{% endcomment %}
    {% if item.image %}
        {% if CLOUDINARY_CONFIGURED %}
            <meta property="og:image" content="{% cloudinary_share_image item.image 'large' %}" />
        {% else %}
            <meta property="og:image" content="{{ request.build_absolute_uri }}{{ item.image.url }}" />
        {% endif %}
    {% endif %}
    <meta property="og:url" content="{{ request.build_absolute_uri }}" />
    <meta property="og:type" content="product" />
{% endblock %}

{% block body %}
<div class="container">
    <!-- Breadcrumb esistente (se presente) -->
    <!-- ... -->
    
    <div class="row">
        <!-- Contenuto principale annuncio -->
        <div class="col-md-8">
            <!-- Dettagli annuncio esistenti -->
            <h1>{{ item.title }}</h1>
            
            <!-- Prezzo evidenziato -->
            <div class="alert alert-success">
                <h3 class="mb-0">💶 {{ item.price }}€</h3>
            </div>
            
            <!-- 📷 GALLERIA IMMAGINI CON CLOUDINARY OTTIMIZZATA -->
            {% if item.image_set.all %}
                <div class="row mb-4">
                    {% for image in item.image_set.all %}
                        <div class="col-md-4 mb-2">
                            {% comment %}⭐ USA CLOUDINARY SE CONFIGURATO, ALTRIMENTI FALLBACK{% endcomment %}
                            {% if CLOUDINARY_CONFIGURED %}
                                <a href="{% cloudinary_url image.file 'large' %}" data-lightbox="gallery" data-title="Immagine {{ forloop.counter }}">
                                    {% cloudinary_img image.file item.title "img-fluid rounded shadow-sm" "medium" %}
                                </a>
                            {% else %}
                                <a href="{{ image.file.url }}" data-lightbox="gallery">
                                    <img src="{{ image.file.url }}" alt="{{ item.title }}" 
                                         class="img-fluid rounded shadow-sm" loading="lazy">
                                </a>
                            {% endif %}
                        </div>
                    {% endfor %}
                </div>
            {% elif item.image %}
                <!-- Immagine singola principale -->
                <div class="main-image-container mb-4">
                    {% if CLOUDINARY_CONFIGURED %}
                        <a href="{% cloudinary_url item.image 'large' %}" data-lightbox="main-image">
                            {% cloudinary_img item.image item.title "img-fluid rounded shadow-lg" "large" %}
                        </a>
                    {% else %}
                        <a href="{{ item.image.url }}" data-lightbox="main-image">
                            <img src="{{ item.image.url }}" alt="{{ item.title }}" 
                                 class="img-fluid rounded shadow-lg" loading="lazy">
                        </a>
                    {% endif %}
                </div>
            {% else %}
                <!-- Nessuna immagine -->
                <div class="no-image-placeholder text-center bg-light rounded p-5 mb-4">
                    <i class="fas fa-image fa-3x text-muted mb-3"></i>
                    <p class="text-muted">Nessuna immagine disponibile</p>
                </div>
            {% endif %}
            
            <!-- Descrizione -->
            {% if item.description %}
                <div class="card mb-4">
                    <div class="card-header">
                        <h5>📝 Descrizione</h5>
                    </div>
                    <div class="card-body">
                        {{ item.description|linebreaks }}
                    </div>
                </div>
            {% endif %}
            
            <!-- Dettagli tecnici -->
            <div class="card mb-4">
                <div class="card-header">
                    <h5>ℹ️ Dettagli</h5>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-6">
                            <p><strong>📅 Pubblicato:</strong> {{ item.created|date:"d/m/Y" }}</p>
                            <p><strong>👤 Venditore:</strong> {{ item.user.username }}</p>
                        </div>
                        <div class="col-md-6">
                            {% if item.area %}
                                <p><strong>📍 Area:</strong> {{ item.area }}</p>
                            {% endif %}
                            {% if item.group %}
                                <p><strong>📂 Categoria:</strong> {{ item.group }}</p>
                            {% endif %}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Sidebar azioni -->
        <div class="col-md-4">
            <!-- 🎮 SEZIONE AZIONI PRINCIPALE -->
            <div class="card mb-3">
                <div class="card-header bg-primary text-white">
                    <h5>🎮 Ottieni questo articolo</h5>
                </div>
                <div class="card-body">
                    {% if user.is_authenticated and item.user != user %}
                        
                        <!-- Verifica disponibilità -->
                        {% if item.is_active %}
                            <div class="alert alert-success">
                                <strong>✅ Disponibile</strong>
                            </div>
                            
                            <!-- 💰 PULSANTE ACQUISTA SUBITO -->
                            {% if item.user.seller_profile and item.user.seller_profile.accepts_payments %}
                                <a href="{% url 'payments:request_purchase' item.pk %}" 
                                   class="btn btn-success btn-lg btn-block mb-3">
                                    💰 Acquista Subito - {{ item.price }}€
                                </a>
                                <p class="text-muted small text-center">Pagamento sicuro con Stripe</p>
                                
                                <hr>
                            {% else %}
                                <!-- Link per creare/configurare il profilo venditore -->
                                {% if user == item.user %}
                                    <div class="alert alert-info mb-3">
                                        <small>
                                            Per vendere online, 
                                            <a href="{% url 'payments:seller_setup' %}">configura le tue impostazioni di pagamento</a>
                                        </small>
                                    </div>
                                {% else %}
                                    <div class="alert alert-warning mb-3">
                                        <small>⚠️ Questo venditore accetta solo scambi</small>
                                    </div>
                                {% endif %}
                            {% endif %}
                            
                            <!-- 🔄 PULSANTE PROPONI SCAMBIO -->
                            <a href="{% url 'trade:propose' item.pk %}" 
                               class="btn btn-primary btn-lg btn-block mb-2">
                                🔄 Proponi Scambio
                            </a>
                            <p class="text-muted small text-center">Scambia con un tuo articolo</p>
                            
                        {% else %}
                            <!-- Annuncio non disponibile -->
                            <div class="alert alert-warning">
                                <strong>⏳ Non Disponibile</strong>
                                <p class="mb-0">Questo articolo è già stato venduto o riservato.</p>
                            </div>
                        {% endif %}
                        
                    {% elif user.is_authenticated and item.user == user %}
                        <!-- È il tuo annuncio -->
                        <div class="alert alert-info">
                            <strong>👤 Il Tuo Annuncio</strong>
                            <p class="mb-2">Gestisci il tuo annuncio:</p>
                            <a href="{% url 'django_classified:item-edit' item.pk %}" 
                               class="btn btn-outline-primary btn-sm">✏️ Modifica</a>
                        </div>
                        
                    {% else %}
                        <!-- Utente non autenticato -->
                        <div class="alert alert-warning">
                            <strong>🔐 Accesso Richiesto</strong>
                            <p class="mb-2">Per acquistare o proporre scambi devi essere registrato.</p>
                            <div class="btn-group btn-group-sm" role="group">
                                <a href="{% url 'login' %}" class="btn btn-primary">Accedi</a>
                                <a href="{% url 'registration_register' %}" class="btn btn-outline-primary">Registrati</a>
                            </div>
                        </div>
                    {% endif %}
                </div>
            </div>
            
            <!-- 📊 INFORMAZIONI VENDITORE -->
            <div class="card mb-3">
                <div class="card-header">
                    <h6>👤 Informazioni Venditore</h6>
                </div>
                <div class="card-body">
                    <div class="seller-profile d-flex align-items-center mb-3">
                        <div class="seller-avatar me-3">
                            <div class="avatar-circle bg-primary text-white d-flex align-items-center justify-content-center">
                                {{ item.user.username|first|upper }}
                            </div>
                        </div>
                        <div>
                            <h6 class="mb-1">{{ item.user.username }}</h6>
                            {% if item.user.trade_profile %}
                                <small class="text-muted">
                                    ⭐ {{ item.user.trade_profile.average_rating|floatformat:1 }}/5
                                    ({{ item.user.trade_profile.total_feedbacks_received }} recensioni)
                                </small>
                            {% endif %}
                        </div>
                    </div>
                    
                    {% if item.user.seller_profile %}
                        {% if item.user.seller_profile.total_sales > 0 %}
                            <div class="row text-center">
                                <div class="col-6">
                                    <small class="text-muted">Vendite</small><br>
                                    <strong>{{ item.user.seller_profile.total_sales }}</strong>
                                </div>
                                <div class="col-6">
                                    <small class="text-muted">Rating</small><br>
                                    <strong>⭐ {{ item.user.seller_profile.average_rating|floatformat:1 }}/5</strong>
                                </div>
                            </div>
                        {% else %}
                            <p class="text-muted small">Nuovo venditore</p>
                        {% endif %}
                        
                        <!-- Modalità di pagamento accettate -->
                        <hr>
                        <h6 class="small">💳 Pagamenti Accettati:</h6>
                        {% if item.user.seller_profile.accepts_payments %}
                            <span class="badge badge-success">✅ Pagamenti Online</span><br>
                        {% else %}
                            <span class="badge badge-secondary">❌ Solo Scambi</span><br>
                        {% endif %}
                        <span class="badge badge-info">🔄 Baratto</span>
                        
                        <!-- Statistiche Scambi -->
                        {% if item.user.trade_profile %}
                            <div class="seller-stats mt-2">
                                <small class="text-muted">
                                    🔄 {{ item.user.trade_profile.total_trades_completed }} scambi completati
                                </small>
                            </div>
                        {% endif %}
                    {% endif %}
                </div>
            </div>
            
            <!-- 📤 CONDIVISIONE SOCIAL -->
            <div class="card mb-3">
                <div class="card-header">
                    <h6>📤 Condividi</h6>
                </div>
                <div class="card-body">
                    <div class="btn-group btn-group-sm btn-block" role="group">
                        <button type="button" class="btn btn-outline-primary" onclick="shareOnFacebook()">
                            📘 Facebook
                        </button>
                        <button type="button" class="btn btn-outline-info" onclick="shareOnTwitter()">
                            🐦 Twitter
                        </button>
                        <button type="button" class="btn btn-outline-success" onclick="shareOnWhatsApp()">
                            💚 WhatsApp
                        </button>
                        <button type="button" class="btn btn-outline-secondary" onclick="copyLink()">
                            🔗 Link
                        </button>
                    </div>
                </div>
            </div>
            
            <!-- 💡 COME FUNZIONA -->
            <div class="card">
                <div class="card-header">
                    <h6>💡 Come Funziona</h6>
                </div>
                <div class="card-body">
                    <div class="accordion" id="howItWorks">
                        
                        <!-- Acquisto -->
                        {% if item.user.seller_profile.accepts_payments %}
                        <div class="card border-0">
                            <div class="card-header p-0" id="headingBuy">
                                <button class="btn btn-link text-left" type="button" 
                                        data-toggle="collapse" data-target="#collapseBuy"
                                        aria-expanded="false" aria-controls="collapseBuy">
                                    💰 <strong>Acquisto Diretto</strong>
                                </button>
                            </div>
                            <div id="collapseBuy" class="collapse" data-parent="#howItWorks">
                                <div class="card-body p-2">

<<TRUNCATED FILE: limited to 300 lines>>
```


---

## Git History (last 50 commits)

```
* 8c050fd 2025-09-03  (HEAD -> cloudinary, origin/cloudinary) Add Cloudinary integration for image management
* 3823529 2025-09-03  (origin/master, origin/HEAD, master) Refactor payments logic and improve Stripe webhook handling
* 4b9ebf1 2025-09-03  Fix purchase flow and history, improve Stripe webhook
* 8234b2e 2025-09-03  Enhance payments: active requests, stats, and UX improvements
* 90df6c2 2025-09-03  Enhance payments: add active requests, stats, and UX improvements
* afaea22 2025-09-03  Add payments app and integrate barter system
*   01abd74 2025-09-02  Merge branch 'baratto' into master
|\  
| * fdf3425 2025-09-02  Add media URL serving in DEBUG mode
| * 2b09447 2025-09-02  Aggiungi supporto immagini alla messaggistica degli scambi
| * c1af384 2025-09-01  Refactor TradeProposal state management to use CharField
| * 1adefaf 2025-09-01  Add project snapshot and trade module integration
| * 1c788d0 2025-08-31  Move registration templates and add base.html bridge
| * eff7548 2025-08-31  Add trade (barter) module with user proposals
|/  
* 1f7483b 2025-08-31  (origin/custom_ninvendo, custom_ninvendo) Add NINVENDO branding and dynamic site config support
* eea7fe8 2025-08-31  Add list_html.txt and list_py.txt files
* a484832 2025-08-31  (custom) Set local memory cache backend for development
* 48bd3b2 2025-04-03  (upstream/master, upstream/HEAD) Bump django from 5.1.7 to 5.1.8 (#173)
* 11cf76a 2025-03-11  Bump django from 5.1.5 to 5.1.7 (#172)
* 6f541c1 2025-01-26  Bump django from 5.1.4 to 5.1.5 (#168)
* ed34e86 2025-01-06  Update deployment template to use repo_clone_url instead of github
* 1d50510 2025-01-05  Digital Ocean deployment button (#166)
* 3187eb1 2025-01-05  Update project configuration and dependencies
*   36aba25 2023-07-25  Merge pull request #163 from slyapustin/dependabot/pip/django-3.2.18
|\  
| * d8cc25f 2023-02-15  Bump django from 3.2.15 to 3.2.18
* |   7c01deb 2023-07-25  Merge pull request #164 from slyapustin/dokku
|\ \  
| |/  
|/|   
| * 859b9ec 2023-07-25  Set DEFAULT_AUTO_FIELD config option.
| * 56f95cd 2023-07-25  Updated Python version.
|/  
*   3c799bf 2022-08-11  Merge pull request #159 from slyapustin/dependabot/pip/django-3.2.15
|\  
| * 251e0e3 2022-08-11  Bump django from 3.2.14 to 3.2.15
|/  
* b9de3ef 2022-07-17  Updated Python
*   c74a3a1 2022-07-17  Merge branch 'master' of github.com:inoks/django-classified-demo
|\  
| *   0c49ac9 2022-05-07  Merge pull request #158 from slyapustin/dependabot/pip/django-3.1.14
| |\  
| | * 965588c 2022-05-07  Bump django from 3.1.13 to 3.1.14
| |/  
| *   5d17ec8 2022-05-07  Merge pull request #145 from slyapustin/dependabot/pip/django-3.1.13
| |\  
| | * 3769a97 2021-09-22  Bump django from 3.0.9 to 3.1.13
| |/  
| *   6f5633d 2020-12-23  Merge pull request #109 from slyapustin/pyup-update-whitenoise-5.1.0-to-5.2.0
| |\  
| | * c8d73c9 2020-08-04  (upstream/pyup-update-whitenoise-5.1.0-to-5.2.0) Update whitenoise from 5.1.0 to 5.2.0
| * |   1440971 2020-12-23  Merge pull request #112 from slyapustin/pyup-update-psycopg2-binary-2.8.5-to-2.8.6
| |\ \  
| | * | 2132003 2020-09-07  (upstream/pyup-update-psycopg2-binary-2.8.5-to-2.8.6) Update psycopg2-binary from 2.8.5 to 2.8.6
| | |/  
| * |   3841296 2020-12-23  Merge pull request #114 from praveenmylavarapu/master
| |\ \  
| | * | 50e6a40 2020-10-01  Read .env file
| | |/  
| * |   1a291c5 2020-12-17  Merge pull request #118 from slyapustin/pyup-update-django-storages-1.9.1-to-1.11
| |\ \  
| | |/  
| |/|   
| | * 0f34723 2020-12-17  Update django-storages from 1.9.1 to 1.11
| |/  
| *   fa4bd1d 2020-08-04  Merge pull request #107 from slyapustin/pyup-update-django-3.0.7-to-3.0.9
| |\  
| | * 72d7097 2020-08-03  (upstream/pyup-update-django-3.0.7-to-3.0.9) Update django from 3.0.7 to 3.0.9
| |/  
| *   32a72b2 2020-06-04  Merge pull request #104 from slyapustin/pyup-update-django-3.0.6-to-3.0.7
| |\  
| | * 58b54dd 2020-06-03  Update django from 3.0.6 to 3.0.7
| |/  
| *   6ec458d 2020-05-21  Merge pull request #102 from slyapustin/pyup-update-whitenoise-5.0.1-to-5.1.0
| |\  
| | * 2614398 2020-05-20  Update whitenoise from 5.0.1 to 5.1.0
| |/  
| *   81ccf2a 2020-05-04  Merge pull request #98 from slyapustin/pyup-update-django-3.0.5-to-3.0.6
| |\
```


---

## Templates Snapshot


### demo/templates/demo/login.html

```html
{% extends 'django_classified/_base.html' %}

{% load i18n %}

{% block title %}{% trans "Login" %}{% endblock title %}

{% block body %}

  <div class="row">
    <div class="col-lg-12">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title">{% trans "Login" %}</h4>
          </div>
          <div class="modal-body">
            <ul>
              <li><a href="{% url "social:begin" "facebook" %}">Facebook</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>

{% endblock %}
```


### templates/base.html

```html
{% extends "django_classified/_base.html" %}

{# This template serves as a bridge between django-registration 
   and your existing _base.html template structure #}
```


### templates/cloudinary/image_gallery.html

```html
{% load cloudinary_tags %}

<div class="cloudinary-gallery">
    <div class="row">
        {% for image in images %}
            <div class="{{ thumbnail_class }} mb-3">
                <div class="image-container position-relative">
                    {% if lightbox %}
                        <a href="{% cloudinary_url image 'large' %}" 
                           data-lightbox="gallery" 
                           data-title="Immagine {{ forloop.counter }}">
                            {% cloudinary_img image "Immagine prodotto" "img-fluid rounded shadow-sm" "medium" %}
                        </a>
                    {% else %}
                        {% cloudinary_img image "Immagine prodotto" "img-fluid rounded shadow-sm" "medium" %}
                    {% endif %}
                    
                    <!-- Overlay info se necessario -->
                    <div class="image-overlay position-absolute" style="bottom: 5px; right: 5px;">
                        <span class="badge badge-dark">{{ forloop.counter }}/{{ images.count }}</span>
                    </div>
                </div>
            </div>
        {% empty %}
            <div class="col-12 text-center">
                <div class="no-images-placeholder p-4 bg-light rounded">
                    <i class="fas fa-images fa-3x text-muted mb-2"></i>
                    <p class="text-muted mb-0">Nessuna immagine disponibile</p>
                </div>
            </div>
        {% endfor %}
    </div>
</div>

{% if lightbox and images %}
    <!-- Includi Lightbox CSS/JS se non già presente -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/js/lightbox.min.js"></script>
    
    <script>
        // Configurazione Lightbox
        lightbox.option({
            'resizeDuration': 200,
            'wrapAround': true,
            'fadeDuration': 300
        });
    </script>
{% endif %}

<style>
    .cloudinary-gallery .image-container {
        overflow: hidden;
        border-radius: 0.5rem;
        transition: transform 0.3s ease;
    }
    
    .cloudinary-gallery .image-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .no-images-placeholder {
        border: 2px dashed #dee2e6;
    }
    
    .image-overlay {
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .image-container:hover .image-overlay {
        opacity: 1;
    }
</style>
```


### templates/debug_cloudinary.html

```html
{% extends "django_classified/_base.html" %}
{% load cloudinary %}

{% block title %}🔧 Debug Cloudinary - {{ SITE_NAME }}{% endblock %}

{% block body %}
<div class="container mt-4">
    <h1>🔧 Debug Cloudinary</h1>
    
    <!-- Info Sito -->
    <div class="card mb-4">
        <div class="card-header bg-info text-white">
            <h5>🏠 Configurazione Sito</h5>
        </div>
        <div class="card-body">
            <p><strong>Nome:</strong> {{ SITE_NAME }}</p>
            <p><strong>Descrizione:</strong> {{ SITE_DESCRIPTION }}</p>
            <p><strong>Tagline:</strong> {{ SITE_TAGLINE }}</p>
            <p><strong>URL:</strong> {{ SITE_URL }}</p>
            <p><strong>Debug Mode:</strong> {{ DEBUG|yesno:"✅ Attivo,❌ Disattivo" }}</p>
        </div>
    </div>

    <!-- Status Cloudinary -->
    <div class="card mb-4">
        <div class="card-header bg-primary text-white">
            <h5>☁️ Status Cloudinary</h5>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-md-6">
                    <p><strong>Configurato:</strong> 
                        <span class="badge badge-{{ CLOUDINARY_CONFIGURED|yesno:'success,danger' }}">
                            {{ CLOUDINARY_CONFIGURED|yesno:"✅ SI,❌ NO" }}
                        </span>
                    </p>
                    <p><strong>Attivo:</strong> 
                        <span class="badge badge-{{ CLOUDINARY_ACTIVE|yesno:'success,warning' }}">
                            {{ CLOUDINARY_ACTIVE|yesno:"🌥️ Cloudinary,📁 Filesystem" }}
                        </span>
                    </p>
                    <p><strong>Dev Mode:</strong> 
                        <span class="badge badge-{{ USE_CLOUDINARY_IN_DEV|yesno:'info,secondary' }}">
                            {{ USE_CLOUDINARY_IN_DEV|yesno:"🧪 Test Mode,📁 Locale" }}
                        </span>
                    </p>
                </div>
                <div class="col-md-6">
                    {% if CLOUDINARY_TRANSFORMATIONS %}
                        <p><strong>Trasformazioni:</strong></p>
                        <ul class="small">
                            {% for name, config in CLOUDINARY_TRANSFORMATIONS.items %}
                                <li>{{ name }}: {{ config.width }}x{{ config.height }}</li>
                            {% endfor %}
                        </ul>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>

    <!-- Test Template Tags -->
    {% if CLOUDINARY_CONFIGURED %}
        <div class="card mb-4">
            <div class="card-header bg-success text-white">
                <h5>🏷️ Test Template Tags</h5>
            </div>
            <div class="card-body">
                <p>I template tags Cloudinary sono disponibili:</p>
                <ul>
                    <li>✅ <code>{% templatetag openblock %} load cloudinary_tags {% templatetag closeblock %}</code></li>
                    <li>✅ <code>{% templatetag openblock %} cloudinary_img item.image {% templatetag closeblock %}</code></li>
                    <li>✅ <code>{% templatetag openblock %} cloudinary_url item.image 'medium' {% templatetag closeblock %}</code></li>
                </ul>
                
                <!-- Test immagine se disponibile -->
                {% comment %}
                Se hai un'immagine di test puoi decommentare:
                {% if test_item.image %}
                    <div class="mt-3">
                        <h6>Esempio Immagine:</h6>
                        {% cloudinary_img test_item.image "Test image" "img-fluid" "medium" %}
                    </div>
                {% endif %}
                {% endcomment %}
            </div>
        </div>
    {% else %}
        <div class="card mb-4">
            <div class="card-header bg-warning text-white">
                <h5>⚠️ Cloudinary Non Configurato</h5>
            </div>
            <div class="card-body">
                <p>Per attivare Cloudinary:</p>
                <ol>
                    <li>Configura le variabili d'ambiente nel <code>.env</code>:
                        <pre class="bg-light p-2 mt-2">
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
USE_CLOUDINARY_IN_DEV=True</pre>
                    </li>
                    <li>Riavvia il server: <code>python manage.py runserver</code></li>
                    <li>Testa: <code>python manage.py cloudinary_admin status</code></li>
                </ol>
            </div>
        </div>
    {% endif %}

    <!-- Comandi Utili -->
    <div class="card mb-4">
        <div class="card-header bg-dark text-white">
            <h5>🛠️ Comandi Utili</h5>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-md-6">
                    <h6>Verifica:</h6>
                    <pre class="bg-light p-2 small">python manage.py cloudinary_admin status</pre>
                    
                    <h6>Test:</h6>
                    <pre class="bg-light p-2 small">python manage.py cloudinary_admin test</pre>
                </div>
                <div class="col-md-6">
                    <h6>Migrazione:</h6>
                    <pre class="bg-light p-2 small">python manage.py cloudinary_admin migrate --limit 10</pre>
                    
                    <h6>Statistiche:</h6>
                    <pre class="bg-light p-2 small">python manage.py cloudinary_admin stats</pre>
                </div>
            </div>
        </div>
    </div>

    <!-- Link Utili -->
    <div class="text-center">
        <a href="/" class="btn btn-primary">🏠 Torna alla Home</a>
        <a href="/admin/" class="btn btn-secondary">🔧 Admin</a>
        {% if user.is_staff %}
            <a href="{% url 'django_classified:item-new' %}" class="btn btn-success">➕ Testa Upload Immagine</a>
        {% endif %}
    </div>
</div>

<style>
    pre {
        font-size: 0.9em;
        border-radius: 4px;
    }
    
    .badge {
        font-size: 0.9em;
    }
    
    .card-header h5 {
        margin-bottom: 0;
    }
</style>
{% endblock %}
```


### templates/django_classified/_base.html

```html
{% spaceless %}

  {% load static i18n %}

  <!DOCTYPE HTML>
  <html lang="en">

  <head>
    <title>{% block title %}NINVENDO - A swap and market place for nintendo lovers{% endblock %}</title>

    <meta name="description" content="NINVENDO - A swap and market place for nintendo lovers">
    <meta name="keywords" content="{% block meta_keywords %}{% endblock meta_keywords %}"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% if GOOGLE_SITE_VERIFICATION_ID %}
      <meta name="google-site-verification" content="{{ GOOGLE_SITE_VERIFICATION_ID }}"/>
    {% endif %}
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">

    {% if FACEBOOK_APP_ID %}
      <meta property="fb:app_id" content="{{ FACEBOOK_APP_ID }}"/>
    {% endif %}
    <meta property="og:type" content="website"/>
    {% block meta_og %}{% endblock %}

    <link rel="icon" type="image/x-icon" href="{% static 'django_classified/images/favicon.ico' %}"/>

    <link href="{% static 'django_classified/css/bootstrap.min.css' %}" rel="stylesheet"/>
    <link href="{% static 'django_classified/css/jumbotron-narrow.css' %}" rel="stylesheet"/>
    <link href="{% static 'django_classified/css/lightbox.min.css' %}" rel="stylesheet" type="text/css"/>
    <link href="{% static 'django_classified/css/style.css' %}" rel="stylesheet" type="text/css"/>

    <link rel="alternate" type="application/rss+xml" href="{% url 'django_classified:rss' %}">

  </head>

  <body>
  <div class="container">

    <div class="header clearfix">
      <nav>
        <ul class="nav nav-pills pull-right">
          <li role="presentation" class="active"><a
                  href="{% url 'django_classified:item-new' %}">{% trans "Add new" %}</a>
          </li>
          <li role="presentation"><a href="{% url 'django_classified:index' %}">{% trans "Home" %}</a></li>
          <li role="presentation"><a href="{% url 'django_classified:search' %}">{% trans "Search" %}</a></li>
          {% if user.is_authenticated %}
            <li role="presentation" class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                <span class="glyphicon glyphicon-user"></span> {{ user.username }} <span class="caret"></span>
              </a>
              
            <ul class="dropdown-menu">
                <!-- SEZIONE PERSONALE -->
                <li><a href="{% url 'django_classified:user-items' %}">{% trans "My items" %} ({{ user.item_set.count }})</a></li>
                <li><a href="{% url 'trade:profile' %}">🔧 Il Mio Profilo</a></li>

                <li class="divider"></li>

                <!-- SEZIONE VENDITE -->
                <li class="dropdown-header">🏪 VENDITE</li>
                <li><a href="{% url 'payments:seller_requests' %}">📋 Richieste Ricevute</a></li>
                <li><a href="{% url 'payments:sales_history' %}">💸 Le Mie Vendite</a></li>
                <li><a href="{% url 'payments:seller_setup' %}">⚙️ Impostazioni Vendite</a></li>

                <li class="divider"></li>

                <!-- SEZIONE ACQUISTI -->
                <li class="dropdown-header">🛒 ACQUISTI</li>
                <li><a href="{% url 'payments:purchase_history' %}">💰 I Miei Acquisti</a></li>

                <li class="divider"></li>

                <!-- SEZIONE SCAMBI -->
                <li class="dropdown-header">🔄 SCAMBI</li>
                <li><a href="{% url 'trade:inbox' %}">📥 Scambi (ricevuti)</a></li>
                <li><a href="{% url 'trade:sent' %}">📤 Scambi (inviati)</a></li>

                <li class="divider"></li>
                
                <!-- LOGOUT -->
                <li>
                    <form method="post" action="{% url 'logout' %}" style="margin:0; padding:0;">
                        {% csrf_token %}
                        <button type="submit" class="btn btn-link" style="padding: 0; color: #337ab7;">
                            {% trans "Logout" %}
                        </button>
                    </form>
                </li>
            </ul>
            </li>
          {% else %}
            <li role="presentation">
              <a href="{% url 'django_classified:profile' %}" title="{% trans "Login" %}">
                <span class="glyphicon glyphicon-user"></span> {% trans "Login" %}
              </a>
            </li>
          {% endif %}
        </ul>
      </nav>
      <h4 class="text-muted"><a href="{% url 'django_classified:index' %}">{{ DCF.SITE_NAME }}</a>
        {% if area_list %}
          &nbsp;
          <small>
            <select id="area-selector">
              <option value="">{% trans 'All areas' %}</option>
              {% for area_item in area_list %}
                <option value="{{ area_item.slug }}" {% if area.pk == area_item.pk %}selected{% endif %}>
                  {{ area_item }}
                </option>
              {% endfor %}
            </select>
          </small>
        {% endif %}
      </h4>
    </div>

    {% if messages %}
      {% for message in messages %}
        <div class='row'>
          <div class="col-md-12">
            <div {% if message.tags %} class="alert alert-{{ message.tags }}"{% endif %}>
              <button type="button" class="close" data-dismiss="alert">×</button>
              {{ message|safe }}
            </div>
          </div>
        </div>
      {% endfor %}
    {% endif %}

    {% block body %}

    {% endblock %}

    <footer class="footer">
      <span class="pull-left">{{ DCF.SITE_NAME }}</span>
      {% if DCF.DISPLAY_CREDITS %}
        <span class="pull-right">{% trans "Powered by" %} <a href="https://github.com/slyapustin/NINVENDO"
                                                             title="NINVENDO Ads">NINVENDO Ads (v{{ DCF.VERSION }})</a></span>
      {% endif %}
    </footer>

  </div>

  <script src="{% static 'django_classified/js/jquery-3.3.1.min.js' %}"></script>
  <script src="{% static 'django_classified/js/bootstrap.min.js' %}"></script>
  <script src="{% static 'django_classified/js/lightbox.min.js' %}"></script>

  {% block ext_scripts %}{% endblock %}

  {% if GOOGLE_ANALYTICS_PROPERTY_ID %}
    <script>
      (function (i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] || function () {
          (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date();
        a = s.createElement(o),
            m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
      })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

      ga('create', '{{ GOOGLE_ANALYTICS_PROPERTY_ID }}', 'auto');
      ga('send', 'pageview');
    </script>
  {% endif %}

  <script>
    $(function () {
      $('#area-selector').on('change', function () {
        var params = {
          area_slug: this.value,
          next: window.location.href
        };
        window.location = "{% url 'django_classified:set-area' %}?" + $.param(params);
      });
    });
  </script>

  <!-- generated {% now "jS F Y H:i:s" %} -->
  </body>
  </html>
{% endspaceless %}
```


### templates/django_classified/item_detail.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n %}
{% comment %}⭐ CARICA CLOUDINARY TAGS SE DISPONIBILI{% endcomment %}
{% load cloudinary_tags %}

{% block title %}{{ item.title }} - {{ item.price }}€{% endblock %}

{% block meta_keywords %}{{ item.title }}, {{ item.area.title }}, {{ item.category.title }}, {{ item.group.title }}{% endblock meta_keywords %}

{% block meta_og %}
    <meta property="og:title" content="{{ item.title }}" />
    <meta property="og:description" content="{{ item.description|truncatewords:30|striptags }}" />
    {% comment %}⭐ USA CLOUDINARY PER IMMAGINI SOCIAL SE DISPONIBILE{% endcomment %}
    {% if item.image %}
        {% if CLOUDINARY_CONFIGURED %}
            <meta property="og:image" content="{% cloudinary_share_image item.image 'large' %}" />
        {% else %}
            <meta property="og:image" content="{{ request.build_absolute_uri }}{{ item.image.url }}" />
        {% endif %}
    {% endif %}
    <meta property="og:url" content="{{ request.build_absolute_uri }}" />
    <meta property="og:type" content="product" />
{% endblock %}

{% block body %}
<div class="container">
    <!-- Breadcrumb esistente (se presente) -->
    <!-- ... -->
    
    <div class="row">
        <!-- Contenuto principale annuncio -->
        <div class="col-md-8">
            <!-- Dettagli annuncio esistenti -->
            <h1>{{ item.title }}</h1>
            
            <!-- Prezzo evidenziato -->
            <div class="alert alert-success">
                <h3 class="mb-0">💶 {{ item.price }}€</h3>
            </div>
            
            <!-- 📷 GALLERIA IMMAGINI CON CLOUDINARY OTTIMIZZATA -->
            {% if item.image_set.all %}
                <div class="row mb-4">
                    {% for image in item.image_set.all %}
                        <div class="col-md-4 mb-2">
                            {% comment %}⭐ USA CLOUDINARY SE CONFIGURATO, ALTRIMENTI FALLBACK{% endcomment %}
                            {% if CLOUDINARY_CONFIGURED %}
                                <a href="{% cloudinary_url image.file 'large' %}" data-lightbox="gallery" data-title="Immagine {{ forloop.counter }}">
                                    {% cloudinary_img image.file item.title "img-fluid rounded shadow-sm" "medium" %}
                                </a>
                            {% else %}
                                <a href="{{ image.file.url }}" data-lightbox="gallery">
                                    <img src="{{ image.file.url }}" alt="{{ item.title }}" 
                                         class="img-fluid rounded shadow-sm" loading="lazy">
                                </a>
                            {% endif %}
                        </div>
                    {% endfor %}
                </div>
            {% elif item.image %}
                <!-- Immagine singola principale -->
                <div class="main-image-container mb-4">
                    {% if CLOUDINARY_CONFIGURED %}
                        <a href="{% cloudinary_url item.image 'large' %}" data-lightbox="main-image">
                            {% cloudinary_img item.image item.title "img-fluid rounded shadow-lg" "large" %}
                        </a>
                    {% else %}
                        <a href="{{ item.image.url }}" data-lightbox="main-image">
                            <img src="{{ item.image.url }}" alt="{{ item.title }}" 
                                 class="img-fluid rounded shadow-lg" loading="lazy">
                        </a>
                    {% endif %}
                </div>
            {% else %}
                <!-- Nessuna immagine -->
                <div class="no-image-placeholder text-center bg-light rounded p-5 mb-4">
                    <i class="fas fa-image fa-3x text-muted mb-3"></i>
                    <p class="text-muted">Nessuna immagine disponibile</p>
                </div>
            {% endif %}
            
            <!-- Descrizione -->
            {% if item.description %}
                <div class="card mb-4">
                    <div class="card-header">
                        <h5>📝 Descrizione</h5>
                    </div>
                    <div class="card-body">
                        {{ item.description|linebreaks }}
                    </div>
                </div>
            {% endif %}
            
            <!-- Dettagli tecnici -->
            <div class="card mb-4">
                <div class="card-header">
                    <h5>ℹ️ Dettagli</h5>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-6">
                            <p><strong>📅 Pubblicato:</strong> {{ item.created|date:"d/m/Y" }}</p>
                            <p><strong>👤 Venditore:</strong> {{ item.user.username }}</p>
                        </div>
                        <div class="col-md-6">
                            {% if item.area %}
                                <p><strong>📍 Area:</strong> {{ item.area }}</p>
                            {% endif %}
                            {% if item.group %}
                                <p><strong>📂 Categoria:</strong> {{ item.group }}</p>
                            {% endif %}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Sidebar azioni -->
        <div class="col-md-4">
            <!-- 🎮 SEZIONE AZIONI PRINCIPALE -->
            <div class="card mb-3">
                <div class="card-header bg-primary text-white">
                    <h5>🎮 Ottieni questo articolo</h5>
                </div>
                <div class="card-body">
                    {% if user.is_authenticated and item.user != user %}
                        
                        <!-- Verifica disponibilità -->
                        {% if item.is_active %}
                            <div class="alert alert-success">
                                <strong>✅ Disponibile</strong>
                            </div>
                            
                            <!-- 💰 PULSANTE ACQUISTA SUBITO -->
                            {% if item.user.seller_profile and item.user.seller_profile.accepts_payments %}
                                <a href="{% url 'payments:request_purchase' item.pk %}" 
                                   class="btn btn-success btn-lg btn-block mb-3">
                                    💰 Acquista Subito - {{ item.price }}€
                                </a>
                                <p class="text-muted small text-center">Pagamento sicuro con Stripe</p>
                                
                                <hr>
                            {% else %}
                                <!-- Link per creare/configurare il profilo venditore -->
                                {% if user == item.user %}
                                    <div class="alert alert-info mb-3">
                                        <small>
                                            Per vendere online, 
                                            <a href="{% url 'payments:seller_setup' %}">configura le tue impostazioni di pagamento</a>
                                        </small>
                                    </div>
                                {% else %}
                                    <div class="alert alert-warning mb-3">
                                        <small>⚠️ Questo venditore accetta solo scambi</small>
                                    </div>
                                {% endif %}
                            {% endif %}
                            
                            <!-- 🔄 PULSANTE PROPONI SCAMBIO -->
                            <a href="{% url 'trade:propose' item.pk %}" 
                               class="btn btn-primary btn-lg btn-block mb-2">
                                🔄 Proponi Scambio
                            </a>
                            <p class="text-muted small text-center">Scambia con un tuo articolo</p>
                            
                        {% else %}
                            <!-- Annuncio non disponibile -->
                            <div class="alert alert-warning">
                                <strong>⏳ Non Disponibile</strong>
                                <p class="mb-0">Questo articolo è già stato venduto o riservato.</p>
                            </div>
                        {% endif %}
                        
                    {% elif user.is_authenticated and item.user == user %}
                        <!-- È il tuo annuncio -->
                        <div class="alert alert-info">
                            <strong>👤 Il Tuo Annuncio</strong>
                            <p class="mb-2">Gestisci il tuo annuncio:</p>
                            <a href="{% url 'django_classified:item-edit' item.pk %}" 
                               class="btn btn-outline-primary btn-sm">✏️ Modifica</a>
                        </div>
                        
                    {% else %}
                        <!-- Utente non autenticato -->
                        <div class="alert alert-warning">
                            <strong>🔐 Accesso Richiesto</strong>
                            <p class="mb-2">Per acquistare o proporre scambi devi essere registrato.</p>
                            <div class="btn-group btn-group-sm" role="group">
                                <a href="{% url 'login' %}" class="btn btn-primary">Accedi</a>
                                <a href="{% url 'registration_register' %}" class="btn btn-outline-primary">Registrati</a>
                            </div>
                        </div>
                    {% endif %}
                </div>
            </div>
            
            <!-- 📊 INFORMAZIONI VENDITORE -->
            <div class="card mb-3">
                <div class="card-header">
                    <h6>👤 Informazioni Venditore</h6>
                </div>
                <div class="card-body">
                    <div class="seller-profile d-flex align-items-center mb-3">
                        <div class="seller-avatar me-3">
                            <div class="avatar-circle bg-primary text-white d-flex align-items-center justify-content-center">
                                {{ item.user.username|first|upper }}
                            </div>
                        </div>
                        <div>
                            <h6 class="mb-1">{{ item.user.username }}</h6>
                            {% if item.user.trade_profile %}
                                <small class="text-muted">
                                    ⭐ {{ item.user.trade_profile.average_rating|floatformat:1 }}/5
                                    ({{ item.user.trade_profile.total_feedbacks_received }} recensioni)
                                </small>
                            {% endif %}
                        </div>
                    </div>
                    
                    {% if item.user.seller_profile %}
                        {% if item.user.seller_profile.total_sales > 0 %}
                            <div class="row text-center">
                                <div class="col-6">
                                    <small class="text-muted">Vendite</small><br>
                                    <strong>{{ item.user.seller_profile.total_sales }}</strong>
                                </div>
                                <div class="col-6">
                                    <small class="text-muted">Rating</small><br>
                                    <strong>⭐ {{ item.user.seller_profile.average_rating|floatformat:1 }}/5</strong>
                                </div>
                            </div>
                        {% else %}
                            <p class="text-muted small">Nuovo venditore</p>
                        {% endif %}
                        
                        <!-- Modalità di pagamento accettate -->
                        <hr>
                        <h6 class="small">💳 Pagamenti Accettati:</h6>
                        {% if item.user.seller_profile.accepts_payments %}
                            <span class="badge badge-success">✅ Pagamenti Online</span><br>
                        {% else %}
                            <span class="badge badge-secondary">❌ Solo Scambi</span><br>
                        {% endif %}
                        <span class="badge badge-info">🔄 Baratto</span>
                        
                        <!-- Statistiche Scambi -->
                        {% if item.user.trade_profile %}
                            <div class="seller-stats mt-2">
                                <small class="text-muted">
                                    🔄 {{ item.user.trade_profile.total_trades_completed }} scambi completati
                                </small>
                            </div>
                        {% endif %}
                    {% endif %}
                </div>
            </div>
            
            <!-- 📤 CONDIVISIONE SOCIAL -->
            <div class="card mb-3">
                <div class="card-header">
                    <h6>📤 Condividi</h6>
                </div>
                <div class="card-body">
                    <div class="btn-group btn-group-sm btn-block" role="group">
                        <button type="button" class="btn btn-outline-primary" onclick="shareOnFacebook()">
                            📘 Facebook
                        </button>
                        <button type="button" class="btn btn-outline-info" onclick="shareOnTwitter()">
                            🐦 Twitter
                        </button>
                        <button type="button" class="btn btn-outline-success" onclick="shareOnWhatsApp()">
                            💚 WhatsApp
                        </button>
                        <button type="button" class="btn btn-outline-secondary" onclick="copyLink()">
                            🔗 Link
                        </button>
                    </div>
                </div>
            </div>
            
            <!-- 💡 COME FUNZIONA -->
            <div class="card">
                <div class="card-header">
                    <h6>💡 Come Funziona</h6>
                </div>
                <div class="card-body">
                    <div class="accordion" id="howItWorks">
                        
                        <!-- Acquisto -->
                        {% if item.user.seller_profile.accepts_payments %}
                        <div class="card border-0">
                            <div class="card-header p-0" id="headingBuy">
                                <button class="btn btn-link text-left" type="button" 
                                        data-toggle="collapse" data-target="#collapseBuy"
                                        aria-expanded="false" aria-controls="collapseBuy">
                                    💰 <strong>Acquisto Diretto</strong>
                                </button>
                            </div>
                            <div id="collapseBuy" class="collapse" data-parent="#howItWorks">
                                <div class="card-body p-2">

<<TRUNCATED FILE: limited to 300 lines>>
```


### templates/django_classified/item_form.html

```html
{% extends "django_classified/_base.html" %}

{% load i18n bootstrap %}

{% block title %}{% if form.instance.pk %}{% trans "Edit" %}{% else %}{% trans "Add" %}{% endif %}
  {% trans "item" %}{% endblock title %}

{% block body %}
  <div class="row">
    <div class="col-md-12">
      <form enctype="multipart/form-data" method='post' role="form">
        {{ formset.management_form }}

        {% csrf_token %}

        {{ form|bootstrap }}

        {% for form in formset %}
          {{ form|bootstrap }}
        {% endfor %}
        <input type='submit' class="btn btn-success" value='{% trans "Save" %}'>
      </form>
    </div>
  </div>
{% endblock body %}
```


### templates/django_classified/item_list.html

```html
{% extends "django_classified/_base.html" %}

{% block title %}{{ object }}{% endblock %}

{% block body %}
  <div class="row">
    <div class="col-lg-12">
      <h4>
        <a href="{% url 'django_classified:index' %}#{{ object.section.id }}">{{ object.section }}</a> > <a
              href="{{ object.get_absolute_url }}" title="{{ object.title }}">
          {{ object.title }}
        </a>
      </h4>
    </div>
  </div>

  <div class="row">
    <div class="col-lg-12">
      {% include "django_classified/item_list.inc.html" %}
    </div>
  </div>

  <div class="row">
    <div class="col-lg-12">
      {% include "django_classified/list_pagination.inc.html" %}
    </div>
  </div>
{% endblock body %}
```


### templates/django_classified/login.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n %}

{% block title %}Login{% endblock %}

{% block body %}
<div class="container" style="max-width:400px;margin-top:30px">
  <h3>Accedi</h3>

  <!-- Form username/password -->
  <form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    {{ form.non_field_errors }}

    <div class="form-group">
      <label for="id_username">{% trans "Username" %}</label>
      {{ form.username }} {{ form.username.errors }}
    </div>

    <div class="form-group">
      <label for="id_password">{% trans "Password" %}</label>
      {{ form.password }} {{ form.password.errors }}
    </div>

    <button type="submit" class="btn btn-primary btn-block">{% trans "Entra" %}</button>
  </form>

  <!-- Link reset password -->
  <div style="margin-top:10px;">
    <a href="{% url 'password_reset' %}">{% trans "Password dimenticata?" %}</a>
  </div>

  <!-- Link registrazione -->
  <div style="margin-top:10px;">
    <a href="{% url 'registration_register' %}">{% trans "Non hai un account? Registrati" %}</a>
  </div>

  <hr>

  <!-- Login con Google -->
  <div style="text-align:center;margin-bottom:8px;">
    <a class="btn btn-default" href="{% url 'social:begin' 'google-oauth2' %}?next=/">
      <img src="https://developers.google.com/identity/images/g-logo.png" 
           alt="Google" style="height:18px;vertical-align:middle;margin-right:6px;">
      Accedi con Google
    </a>
  </div>

  <!-- Login con Facebook -->
  <div style="text-align:center;">
    <a class="btn btn-default" href="{% url 'social:begin' 'facebook' %}?next=/">
      Accedi con Facebook
    </a>
  </div>
</div>
{% endblock %}
```


### templates/django_classified/password_reset_complete.html

```html
{% extends "django_classified/_base.html" %}
{% block title %}Password aggiornata{% endblock %}
{% block body %}
<h3>Password aggiornata</h3>
<p>Ora puoi effettuare l’accesso con la nuova password.</p>
<a class="btn btn-default" href="{% url 'login' %}">Vai al login</a>
{% endblock %}
```


### templates/django_classified/password_reset_confirm.html

```html
{% extends "django_classified/_base.html" %}
{% block title %}Imposta nuova password{% endblock %}
{% block body %}
<h3>Imposta una nuova password</h3>
{% if validlink %}
  <form method="post">
    {% csrf_token %}
    {{ form.non_field_errors }}
    <div class="form-group">
      <label for="id_new_password1">Nuova password</label>
      {{ form.new_password1 }}
      {{ form.new_password1.errors }}
    </div>
    <div class="form-group">
      <label for="id_new_password2">Conferma</label>
      {{ form.new_password2 }}
      {{ form.new_password2.errors }}
    </div>
    <button class="btn btn-primary" type="submit">Aggiorna password</button>
  </form>
{% else %}
  <p class="text-warning">Il link non è più valido. Richiedi un nuovo reset.</p>
{% endif %}
{% endblock %}
```


### templates/django_classified/password_reset_done.html

```html
{% extends "django_classified/_base.html" %}
{% block title %}Email inviata{% endblock %}
{% block body %}
<h3>Controlla la tua casella email</h3>
<p>Se l’indirizzo è registrato, abbiamo inviato un link per reimpostare la password.</p>
{% endblock %}
```


### templates/django_classified/password_reset_form.html

```html
{% extends "django_classified/_base.html" %}
{% block title %}Password reset{% endblock %}
{% block body %}
<h3>Password reset</h3>
<p>Inserisci l’email del tuo account. Riceverai un link per reimpostare la password.</p>
<form method="post">
  {% csrf_token %}
  {{ form.email.errors }}
  <div class="form-group">
    <label for="id_email">Email</label>
    {{ form.email }}
  </div>
  <button class="btn btn-primary" type="submit">Invia</button>
</form>
{% endblock %}
```


### templates/django_classified/profile.html

```html
{% extends "django_classified/_base.html" %}

{% load i18n bootstrap %}

{% block title %}{% trans "Profile" %}{% endblock title %}

{% block body %}
  <div class="row marketing">
    <div class="col-lg-12">
      <form method="post" role="form">
        {% csrf_token %}
        {{ form|bootstrap }}
        <input type="submit" value="{% trans "Update" %}" class="btn btn-default">
      </form>
    </div>
  </div>
{% endblock %}
```


### templates/django_classified/search.html

```html
{% extends "django_classified/_base.html" %}

{% load i18n bootstrap %}

{% block title %}
  {% if form.q.value %}{% trans "Search results for query" %} "{{ form.q.value }}" {% else %}
    {% trans "Search" %}{% endif %}
{% endblock title %}

{% block body %}
  <div class="row">
    <div class="col-lg-6">
      <h3>{% trans "Search" %}</h3>
      <form method="get" role="form">
        {{ form|bootstrap }}
        <button type="submit" class="btn btn-default" name="page" value="1">{% trans "Search" %}</button>
        {% if object_list|length %}
          {% include 'django_classified/form_pagination.inc.html' %}
        {% endif %}
      </form>
    </div>
  </div>
  <div>
    <hr/>
    {% if object_list|length %}
      <h4>{% blocktrans with count=page_obj.paginator.count %}Search results ({{ count }} items
        found):{% endblocktrans %}</h4>
      {% include "django_classified/item_list.inc.html" with item=object %}
    {% else %}
      <h4>{% trans "Not found" %}</h4>
    {% endif %}
  </div>
{% endblock %}
```


### templates/django_classified/section_list.html

```html
{% extends "django_classified/_base.html" %}

{% block title %}{{ DCF.SITE_NAME }}{% endblock title %}

{% block body %}
  <div class="row marketing">
    {% for object in object_list %}
      <div class="col-md-3">
        <h4 id="{{ object.section.0.id }}">{{ object.section.0 }} [{{ object.section.1 }}]</h4>
        {% for group, group_count in object.groups %}
          {% if group_count > 0 or DCF.DISPLAY_EMPTY_GROUPS %}
            <a href='{{ group.get_absolute_url }}' title="{{ group.title }}">
              {{ group.title }}&nbsp;[{{ group_count }}]<br/>
            </a>
          {% endif %}
        {% endfor %}
      </div>
    {% endfor %}
  </div>
{% endblock %}
```


### templates/payments/payment_cancelled.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n %}

{% block title %}Pagamento Annullato{% endblock %}

{% block body %}
<div class="container" style="max-width: 600px;">
    <!-- Header Annullamento -->
    <div class="row mb-4">
        <div class="col-md-12">
            <div class="alert alert-warning text-center">
                <h2 class="mb-3">⚠️ Pagamento Annullato</h2>
                <p class="lead mb-0">Il processo di pagamento è stato interrotto.</p>
            </div>
        </div>
    </div>

    <!-- Dettagli Transazione Annullata -->
    <div class="row mb-4">
        <div class="col-md-12">
            <div class="card">
                <div class="card-header bg-warning text-dark">
                    <h5>📄 Dettagli dell'Operazione</h5>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-12">
                            <h6><strong>Articolo:</strong></h6>
                            <p>{{ transaction.item.title }}</p>
                            
                            <h6><strong>Venditore:</strong></h6>
                            <p>{{ transaction.seller.username }}</p>
                            
                            <h6><strong>Importo che avresti pagato:</strong></h6>
                            <p class="text-muted">€{{ transaction.total_amount_euros|floatformat:2 }}</p>
                            
                            <h6><strong>Stato Transazione:</strong></h6>
                            <span class="badge badge-warning">⏸️ Annullato</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Cosa è successo -->
    <div class="row mb-4">
        <div class="col-md-12">
            <div class="card border-info">
                <div class="card-header bg-info text-white">
                    <h6>ℹ️ Cosa è successo?</h6>
                </div>
                <div class="card-body">
                    <p>Il pagamento è stato annullato. I motivi possibili sono:</p>
                    <ul>
                        <li>Hai chiuso la finestra di pagamento</li>
                        <li>Hai cliccato "Indietro" o "Annulla" su Stripe</li>
                        <li>Si è verificato un timeout della sessione</li>
                        <li>Hai deciso di non procedere con l'acquisto</li>
                    </ul>
                    
                    <div class="alert alert-info">
                        <strong>✅ Nessun addebito:</strong> La tua carta non è stata addebitata.
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Cosa fare adesso -->
    <div class="row mb-4">
        <div class="col-md-12">
            <div class="card border-primary">
                <div class="card-header bg-primary text-white">
                    <h6>🤔 Cosa vuoi fare adesso?</h6>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-12 text-center">
                            <p>Puoi:</p>
                            
                            <div class="btn-group-vertical btn-group-lg">
                                <!-- Se la richiesta è ancora approvata, mostra pulsante per riprovare -->
                                {% if transaction.purchase_request.status == 'approved' %}
                                <form method="post" action="{% url 'payments:create_checkout' transaction.purchase_request.uuid %}" class="mb-2">
                                    {% csrf_token %}
                                    <button type="submit" class="btn btn-success btn-lg">
                                        💳 Riprova il Pagamento
                                    </button>
                                </form>
                                {% endif %}
                                
                                <a href="{{ transaction.item.get_absolute_url }}" class="btn btn-secondary btn-lg mb-2">
                                    👁️ Rivedi l'Annuncio
                                </a>
                                
                                <a href="{% url 'payments:purchase_history' %}" class="btn btn-info btn-lg mb-2">
                                    📋 I Miei Acquisti
                                </a>
                                
                                <a href="{% url 'django_classified:index' %}" class="btn btn-primary btn-lg">
                                    🏠 Torna alla Home
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Aiuto -->
    <div class="row">
        <div class="col-md-12">
            <div class="card border-secondary">
                <div class="card-body text-center">
                    <h6>🆘 Problemi tecnici?</h6>
                    <p class="text-muted">
                        Se hai riscontrato errori durante il pagamento,
                        <a href="mailto:support@ninvendo.com">contatta il nostro supporto</a>
                    </p>
                    <p><small>ID Operazione: {{ transaction.uuid|slice:":8" }}</small></p>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
// Rimuovi eventuali parametri di pagamento dall'URL dopo 3 secondi
setTimeout(function() {
    if (window.location.search) {
        window.history.replaceState({}, document.title, window.location.pathname);
    }
}, 3000);
</script>
{% endblock %}
```


### templates/payments/payment_success.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n %}

{% block title %}Pagamento Completato{% endblock %}

{% block body %}
<div class="container" style="max-width: 800px;">
    <!-- Header Successo -->
    <div class="row mb-4">
        <div class="col-md-12">
            <div class="alert alert-success text-center">
                <h2 class="mb-3">🎉 Pagamento Completato!</h2>
                <p class="lead mb-0">Il tuo acquisto è stato elaborato con successo.</p>
            </div>
        </div>
    </div>

    <!-- Dettagli Transazione -->
    <div class="row mb-4">
        <div class="col-md-12">
            <div class="card">
                <div class="card-header bg-success text-white">
                    <h5>📋 Dettagli dell'Acquisto</h5>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-6">
                            <h6><strong>Articolo Acquistato:</strong></h6>
                            <p class="text-primary">{{ transaction.item.title }}</p>
                            
                            <h6><strong>Venditore:</strong></h6>
                            <p>{{ transaction.seller.username }}</p>
                            
                            <h6><strong>Data Acquisto:</strong></h6>
                            <p>{{ transaction.created_at|date:"d/m/Y H:i" }}</p>
                        </div>
                        <div class="col-md-6">
                            <h6><strong>ID Transazione:</strong></h6>
                            <p><code>{{ transaction.uuid|slice:":8" }}</code></p>
                            
                            <h6><strong>Importo Pagato:</strong></h6>
                            <p class="text-success"><strong>€{{ transaction.total_amount_euros|floatformat:2 }}</strong></p>
                            
                            <h6><strong>Stato:</strong></h6>
                            <span class="badge badge-success">✅ Completato</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Breakdown Costi -->
    <div class="row mb-4">
        <div class="col-md-12">
            <div class="card">
                <div class="card-header">
                    <h6>💰 Dettaglio Costi</h6>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-8">
                            <div class="d-flex justify-content-between">
                                <span>Prezzo articolo:</span>
                                <span>€{{ transaction.item_price_euros|floatformat:2 }}</span>
                            </div>
                            <div class="d-flex justify-content-between">
                                <span>Commissione piattaforma (3%):</span>
                                <span>€{{ transaction.platform_fee_euros|floatformat:2 }}</span>
                            </div>
                            <div class="d-flex justify-content-between">
                                <span>Commissione Stripe:</span>
                                <span>€{{ transaction.stripe_fee_euros|floatformat:2 }}</span>
                            </div>
                            <hr>
                            <div class="d-flex justify-content-between">
                                <strong>Totale pagato:</strong>
                                <strong>€{{ transaction.total_amount_euros|floatformat:2 }}</strong>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Informazioni Contatto Venditore -->
    <div class="row mb-4">
        <div class="col-md-12">
            <div class="card border-info">
                <div class="card-header bg-info text-white">
                    <h6>📞 Prossimi Passi</h6>
                </div>
                <div class="card-body">
                    <div class="alert alert-info">
                        <h6>✅ Il tuo pagamento è stato confermato!</h6>
                        <p>Il venditore <strong>{{ transaction.seller.username }}</strong> è stato notificato del tuo acquisto.</p>
                    </div>
                    
                    <h6>Come procedere:</h6>
                    <ol>
                        <li><strong>Contatta il venditore</strong> per accordarvi su spedizione o ritiro</li>
                        <li><strong>Email venditore:</strong> {{ transaction.seller.email }}</li>
                        {% if transaction.shipping_address %}
                        <li><strong>Il tuo indirizzo di spedizione:</strong><br>
                            <code>{{ transaction.shipping_address|linebreaks }}</code>
                        </li>
                        {% endif %}
                        <li>Attendi la consegna o organizza il ritiro</li>
                    </ol>
                    
                    <div class="alert alert-warning">
                        <strong>⚠️ Importante:</strong> Conserva questa pagina come ricevuta del tuo acquisto.
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Azioni Disponibili -->
    <div class="row mb-4">
        <div class="col-md-12">
            <div class="card">
                <div class="card-header">
                    <h6>🔗 Azioni Disponibili</h6>
                </div>
                <div class="card-body text-center">
                    <div class="btn-group btn-group-lg">
                        <a href="{% url 'payments:purchase_history' %}" class="btn btn-primary">
                            📋 I Miei Acquisti
                        </a>
                        
                        <a href="{{ transaction.item.get_absolute_url }}" class="btn btn-secondary">
                            👁️ Vedi Annuncio
                        </a>
                        
                        <a href="{% url 'django_classified:index' %}" class="btn btn-success">
                            🏠 Torna alla Home
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Supporto -->
    <div class="row">
        <div class="col-md-12">
            <div class="card border-secondary">
                <div class="card-body text-center">
                    <h6>🆘 Hai bisogno di aiuto?</h6>
                    <p class="text-muted">
                        Se hai problemi con questo acquisto o domande,
                        <a href="mailto:support@ninvendo.com">contatta il nostro supporto</a>
                    </p>
                    <p><small>ID Transazione: {{ transaction.uuid }}</small></p>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
// Auto-stampa della ricevuta se richiesta
window.onload = function() {
    // Mostra messaggio di successo per 5 secondi
    setTimeout(function() {
        const alert = document.querySelector('.alert-success');
        if (alert) {
            alert.style.transition = 'opacity 0.5s';
            alert.style.opacity = '0.8';
        }
    }, 5000);
};

<<TRUNCATED CONTEXT: limited to 5000 total lines>>