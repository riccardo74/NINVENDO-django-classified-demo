# Project Snapshot

_Generated on 2025-09-04 21:28:12_


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

## Git History (last 50 commits)

```
* da7fa16 2025-09-04  (HEAD -> cloudinary, origin/cloudinary) Add project snapshot improvements and update templates
* 8c050fd 2025-09-03  Add Cloudinary integration for image management
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
{% load static i18n %}
{% comment %}⭐ CARICA CLOUDINARY TAGS SE DISPONIBILI{% endcomment %}
{% load cloudinary %}

{% block title %}{{ item.title }} - {{ item.price }}€{% endblock %}

{% block meta_keywords %}{{ item.title }}, {{ item.area.title }}, {{ item.category.title }}, {{ item.group.title }}{% endblock meta_keywords %}

{% block meta_og %}
    <meta property="og:title" content="{{ item.title }}" />
    <meta property="og:description" content="{{ item.description|truncatewords:30|striptags }}" />
    {% comment %}⭐ USA CLOUDINARY PER IMMAGINI SOCIAL SE DISPONIBILE{% endcomment %}
    {% if item.image %}
        {% if USE_CLOUDINARY %}
            {% cloudinary item.image width=1200 height=630 crop="fill" format="auto" quality="auto:best" as og_image %}
            <meta property="og:image" content="{{ og_image.url }}" />
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
                            {% if USE_CLOUDINARY %}
                                {% cloudinary image.file width=800 height=600 crop="fit" format="auto" quality="auto:best" as large_image %}
                                {% cloudinary image.file width=400 height=300 crop="fill" format="auto" quality="auto:good" as medium_image %}
                                <a href="{{ large_image.url }}" data-lightbox="gallery" data-title="Immagine {{ forloop.counter }}">
                                    <img src="{{ medium_image.url }}" alt="{{ item.title }}" class="img-fluid rounded shadow-sm" loading="lazy">
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
                    {% if USE_CLOUDINARY %}
                        {% cloudinary item.image width=800 height=600 crop="fit" format="auto" quality="auto:best" as large_image %}
                        <a href="{{ large_image.url }}" data-lightbox="main-image">
                            <img src="{{ large_image.url }}" alt="{{ item.title }}" class="img-fluid rounded shadow-lg" loading="lazy">
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
                            <strong>🔒 Accesso Richiesto</strong>
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

// Funzione per stampare la ricevuta
function printReceipt() {
    window.print();
}
</script>

<!-- Print Button (nascosto di default) -->
<div class="d-print-none text-center mb-4">
    <button onclick="printReceipt()" class="btn btn-outline-secondary">
        🖨️ Stampa Ricevuta
    </button>
</div>

<!-- Stile per la stampa -->
<style>
@media print {
    .btn, .card-header, .alert-warning {
        -webkit-print-color-adjust: exact !important;
        color-adjust: exact !important;
    }
    
    .d-print-none {
        display: none !important;
    }
}
</style>
{% endblock %}
```


### templates/payments/purchase_history.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n %}

{% block title %}I Miei Acquisti{% endblock %}

{% block body %}
<div class="container">
    <h3>💰 I Miei Acquisti</h3>
    
    <!-- Statistiche Riepilogo -->
    <div class="row mb-4">
        <div class="col-md-3">
            <div class="card border-primary">
                <div class="card-body text-center">
                    <h4 class="text-primary">{{ pending_requests_count|default:0 }}</h4>
                    <p class="text-muted mb-0">Richieste Pendenti</p>
                </div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card border-success">
                <div class="card-body text-center">
                    <h4 class="text-success">{{ approved_requests_count|default:0 }}</h4>
                    <p class="text-muted mb-0">Richieste Approvate</p>
                </div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card border-info">
                <div class="card-body text-center">
                    <h4 class="text-info">{{ completed_purchases|default:0 }}</h4>
                    <p class="text-muted mb-0">Acquisti Completati</p>
                </div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card border-dark">
                <div class="card-body text-center">
                    <h4 class="text-dark">€{{ total_spent|floatformat:2 }}</h4>
                    <p class="text-muted mb-0">Totale Speso</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Tab Navigation -->
    <ul class="nav nav-tabs mb-4">
        <li class="nav-item">
            <a class="nav-link active" data-toggle="tab" href="#active-requests">
                🔄 Richieste Attive 
                {% if active_requests %}
                    <span class="badge badge-warning">{{ active_requests|length }}</span>
                {% endif %}
            </a>
        </li>
        <li class="nav-item">
            <a class="nav-link" data-toggle="tab" href="#completed-purchases">
                ✅ Acquisti Completati
                {% if transactions %}
                    <span class="badge badge-info">{{ transactions|length }}</span>
                {% endif %}
            </a>
        </li>
    </ul>

    <!-- Tab Content -->
    <div class="tab-content">
        
        <!-- Richieste Attive Tab -->
        <div class="tab-pane fade show active" id="active-requests">
            {% if active_requests %}
                <div class="alert alert-info">
                    <h6>ℹ️ Richieste in Corso</h6>
                    <p class="mb-0">Queste sono le tue richieste di acquisto che stanno ancora aspettando una risposta o il pagamento.</p>
                </div>
                
                <div class="table-responsive">
                    <table class="table table-striped">
                        <thead class="thead-light">
                            <tr>
                                <th>Articolo</th>
                                <th>Venditore</th>
                                <th>Prezzo</th>
                                <th>Stato</th>
                                <th>Creata il</th>
                                <th>Scade il</th>
                                <th>Azioni</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for request in active_requests %}
                            <tr>
                                <td>
                                    <strong>{{ request.item.title|truncatechars:40 }}</strong>
                                    {% if request.item.image_set.first %}
                                        <br><small class="text-muted">📷 Con immagine</small>
                                    {% endif %}
                                </td>
                                <td>{{ request.seller.username }}</td>
                                <td><strong>€{{ request.item.price|floatformat:0 }}</strong></td>
                                <td>
                                    {% if request.status == 'pending' %}
                                        <span class="badge badge-warning">⏳ In Attesa</span>
                                    {% elif request.status == 'approved' %}
                                        <span class="badge badge-success">✅ Approvata</span>
                                    {% endif %}
                                </td>
                                <td>{{ request.created_at|date:"d/m/Y" }}</td>
                                <td>
                                    {% if request.is_expired %}
                                        <span class="badge badge-danger">Scaduta</span>
                                    {% else %}
                                        {{ request.expires_at|date:"d/m/Y" }}
                                    {% endif %}
                                </td>
                                <td>
                                    <div class="btn-group btn-group-sm">
                                        <a href="{% url 'payments:request_detail' request.uuid %}" 
                                           class="btn btn-info btn-sm">👁️ Dettagli</a>
                                        
                                        {% if request.status == 'approved' %}
                                            {% if request.payment_transaction %}
                                                {% if request.payment_transaction.status == 'processing' %}
                                                    <a href="{% url 'payments:payment_success' request.payment_transaction.uuid %}" 
                                                       class="btn btn-warning btn-sm">
                                                        ⏳ In Elaborazione
                                                    </a>
                                                {% elif request.payment_transaction.status == 'succeeded' %}
                                                    <a href="{% url 'payments:payment_success' request.payment_transaction.uuid %}" 
                                                       class="btn btn-success btn-sm">
                                                        ✅ Completato
                                                    </a>
                                                {% else %}
                                                    <form method="post" action="{% url 'payments:create_checkout' request.uuid %}" style="display:inline;">
                                                        {% csrf_token %}
                                                        <button type="submit" class="btn btn-success btn-sm">
                                                            💳 Paga Ora
                                                        </button>
                                                    </form>
                                                {% endif %}
                                            {% else %}
                                                <form method="post" action="{% url 'payments:create_checkout' request.uuid %}" style="display:inline;">
                                                    {% csrf_token %}
                                                    <button type="submit" class="btn btn-success btn-sm">
                                                        💳 Paga Ora
                                                    </button>
                                                </form>
                                            {% endif %}
                                        {% endif %}
                                    </div>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            {% else %}
                <div class="alert alert-secondary">
                    <h4>📭 Nessuna Richiesta Attiva</h4>
                    <p>Non hai richieste di acquisto in corso.</p>
                    <a href="{% url 'django_classified:index' %}" class="btn btn-primary">🛍️ Sfoglia Annunci</a>
                </div>
            {% endif %}
        </div>

        <!-- Acquisti Completati Tab -->
        <div class="tab-pane fade" id="completed-purchases">
            {% if transactions %}
                <div class="table-responsive">
                    <table class="table table-striped">
                        <thead class="thead-dark">
                            <tr>
                                <th>Data</th>
                                <th>Articolo</th>
                                <th>Venditore</th>
                                <th>Importo</th>
                                <th>Stato</th>
                                <th>Azioni</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for transaction in transactions %}
                            <tr>
                                <td>{{ transaction.created_at|date:"d/m/Y H:i" }}</td>
                                <td>
                                    <strong>{{ transaction.item.title|truncatechars:30 }}</strong>
                                    <br><small class="text-muted">#{{ transaction.uuid|slice:":8" }}</small>
                                </td>
                                <td>{{ transaction.seller.username }}</td>
                                <td><strong>€{{ transaction.total_amount_euros|floatformat:2 }}</strong></td>
                                <td>
                                    {% if transaction.status == 'succeeded' %}
                                        <span class="badge badge-success">✅ Completato</span>
                                    {% elif transaction.status == 'processing' %}
                                        <span class="badge badge-warning">⏳ In Elaborazione</span>
                                    {% elif transaction.status == 'pending' %}
                                        <span class="badge badge-info">⏸️ In Attesa</span>
                                    {% elif transaction.status == 'failed' %}
                                        <span class="badge badge-danger">❌ Fallito</span>
                                    {% elif transaction.status == 'cancelled' %}
                                        <span class="badge badge-secondary">🚫 Annullato</span>
                                    {% endif %}
                                </td>
                                <td>
                                    <div class="btn-group btn-group-sm">
                                        <a href="{% url 'payments:payment_success' transaction.uuid %}" 
                                           class="btn btn-secondary btn-sm">📋 Dettagli</a>
                                        
                                        {% if transaction.status == 'succeeded' %}
                                            <span class="btn btn-success btn-sm disabled">✅ Pagato</span>
                                        {% endif %}
                                    </div>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>

                <!-- Paginazione -->
                {% if is_paginated %}
                <div class="text-center">
                    <div class="pagination">
                        {% if page_obj.has_previous %}
                            <a href="?page={{ page_obj.previous_page_number }}">&laquo; Precedente</a>
                        {% endif %}
                        
                        Pagina {{ page_obj.number }} di {{ page_obj.paginator.num_pages }}
                        
                        {% if page_obj.has_next %}
                            <a href="?page={{ page_obj.next_page_number }}">Successiva &raquo;</a>
                        {% endif %}
                    </div>
                </div>
                {% endif %}
                
            {% else %}
                <div class="alert alert-secondary">
                    <h4>📭 Nessun Acquisto Completato</h4>
                    <p>Non hai ancora completato acquisti tramite pagamento.</p>
                    <a href="{% url 'django_classified:index' %}" class="btn btn-primary">🛍️ Inizia a Comprare</a>
                </div>
            {% endif %}
        </div>
    </div>
    
    <!-- Link Utili -->
    <div class="row mt-4">
        <div class="col-md-12">
            <div class="card border-light">
                <div class="card-body">
                    <h6>🔗 Link Utili</h6>
                    <div class="btn-group">
                        <a href="{% url 'payments:seller_setup' %}" class="btn btn-outline-primary">
                            ⚙️ Impostazioni Venditore
                        </a>
                        <a href="{% url 'payments:sales_history' %}" class="btn btn-outline-success">
                            💸 Le Mie Vendite
                        </a>
                        <a href="{% url 'django_classified:index' %}" class="btn btn-outline-info">
                            🏠 Torna alla Home
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
// Auto-refresh richieste ogni 30 secondi se ci sono richieste attive
{% if active_requests %}
setTimeout(function() {
    location.reload();
}, 30000);
{% endif %}

// Tab switching con Bootstrap
$(document).ready(function(){
    $('.nav-tabs a').click(function(e) {
        e.preventDefault();
        $(this).tab('show');
    });
});
</script>
{% endblock %}
```


### templates/payments/request_detail.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n %}

{% block title %}Richiesta #{{ purchase_request.uuid.hex|slice:":8" }}{% endblock %}

{% block body %}
<div class="container">
    <div class="row">
        <div class="col-md-12">
            <!-- Header con stato -->
            <div class="card mb-4">
                <div class="card-header 
                    {% if purchase_request.status == 'pending' %}bg-warning
                    {% elif purchase_request.status == 'approved' %}bg-success text-white
                    {% elif purchase_request.status == 'rejected' %}bg-danger text-white
                    {% elif purchase_request.status == 'completed' %}bg-info text-white
                    {% elif purchase_request.status == 'expired' %}bg-secondary text-white
                    {% endif %}">
                    
                    <div class="row">
                        <div class="col-md-8">
                            <h4>
                                {% if purchase_request.status == 'pending' %}⏳ In Attesa di Approvazione
                                {% elif purchase_request.status == 'approved' %}✅ Richiesta Approvata
                                {% elif purchase_request.status == 'rejected' %}❌ Richiesta Rifiutata
                                {% elif purchase_request.status == 'completed' %}🎉 Acquisto Completato
                                {% elif purchase_request.status == 'expired' %}⌛ Richiesta Scaduta
                                {% endif %}
                            </h4>
                            <p class="mb-0">Richiesta #{{ purchase_request.uuid.hex|slice:":8" }}</p>
                        </div>
                        <div class="col-md-4 text-right">
                            <p class="mb-1"><strong>Data:</strong> {{ purchase_request.created_at|date:"d/m/Y H:i" }}</p>
                            {% if purchase_request.expires_at %}
                                <p class="mb-0"><strong>Scade:</strong> {{ purchase_request.expires_at|date:"d/m/Y H:i" }}</p>
                            {% endif %}
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="row">
                <!-- Dettagli richiesta -->
                <div class="col-md-8">
                    <!-- Informazioni articolo -->
                    <div class="card mb-4">
                        <div class="card-header">
                            <h5>🎮 Articolo Richiesto</h5>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-md-3">
                                    {% if purchase_request.item.image_set.first %}
                                        <img src="{{ purchase_request.item.image_set.first.file.url }}" 
                                             alt="{{ purchase_request.item.title }}" 
                                             class="img-fluid rounded">
                                    {% else %}
                                        <div class="bg-light p-3 text-center rounded">
                                            <span class="text-muted">Nessuna immagine</span>
                                        </div>
                                    {% endif %}
                                </div>
                                <div class="col-md-9">
                                    <h6>{{ purchase_request.item.title }}</h6>
                                    <p class="text-muted">{{ purchase_request.item.description|truncatewords:20 }}</p>
                                    <p><strong>Prezzo:</strong> €{{ purchase_request.item.price }}</p>
                                    <p>
                                        <a href="{{ purchase_request.item.get_absolute_url }}" 
                                           class="btn btn-outline-primary btn-sm">
                                            👁️ Vedi Annuncio Completo
                                        </a>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Informazioni partecipanti -->
                    <div class="row">
                        <!-- Acquirente -->
                        <div class="col-md-6">
                            <div class="card mb-3 {% if is_buyer %}border-primary{% endif %}">
                                <div class="card-header {% if is_buyer %}bg-primary text-white{% endif %}">
                                    <h6>🛒 Acquirente</h6>
                                </div>
                                <div class="card-body">
                                    <p><strong>{{ purchase_request.buyer.username }}</strong>
                                        {% if is_buyer %}<span class="badge badge-primary ml-2">Tu</span>{% endif %}
                                    </p>
                                    <p>📧 {{ purchase_request.buyer.email }}</p>
                                    <p>🚚 {{ purchase_request.get_delivery_method_display }}</p>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Venditore -->
                        <div class="col-md-6">
                            <div class="card mb-3 {% if is_seller %}border-success{% endif %}">
                                <div class="card-header {% if is_seller %}bg-success text-white{% endif %}">
                                    <h6>🏪 Venditore</h6>
                                </div>
                                <div class="card-body">
                                    <p><strong>{{ purchase_request.seller.username }}</strong>
                                        {% if is_seller %}<span class="badge badge-success ml-2">Tu</span>{% endif %}
                                    </p>
                                    {% if purchase_request.seller.seller_profile %}
                                        <p>📊 {{ purchase_request.seller.seller_profile.total_sales }} vendite</p>
                                        <p>⭐ {{ purchase_request.seller.seller_profile.average_rating|floatformat:1 }}/5</p>
                                    {% endif %}
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Indirizzo di spedizione -->
                    {% if purchase_request.shipping_address %}
                    <div class="card mb-3">
                        <div class="card-header">
                            <h6>📍 Indirizzo di Spedizione</h6>
                        </div>
                        <div class="card-body">
                            <address>{{ purchase_request.shipping_address|linebreaks }}</address>
                        </div>
                    </div>
                    {% endif %}
                    
                    <!-- Messaggio dell'acquirente -->
                    {% if purchase_request.message %}
                    <div class="card mb-3">
                        <div class="card-header">
                            <h6>💬 Messaggio dell'Acquirente</h6>
                        </div>
                        <div class="card-body">
                            {{ purchase_request.message|linebreaks }}
                        </div>
                    </div>
                    {% endif %}
                </div>
                
                <!-- Sidebar - Azioni -->
                <div class="col-md-4">
                    <!-- Riepilogo costi -->
                    <div class="card mb-3">
                        <div class="card-header">
                            <h6>💳 Riepilogo Costi</h6>
                        </div>
                        <div class="card-body">
                            <table class="table table-sm">
                                <tbody>
                                    <tr>
                                        <td>Prezzo articolo:</td>
                                        <td class="text-right"><strong>€{{ fees.item_price_euros|floatformat:2 }}</strong></td>
                                    </tr>
                                    <tr>
                                        <td>Commissione piattaforma (3%):</td>
                                        <td class="text-right">€{{ fees.platform_fee_euros|floatformat:2 }}</td>
                                    </tr>
                                    <tr>
                                        <td>Commissione Stripe:</td>
                                        <td class="text-right">€{{ fees.stripe_fee_euros|floatformat:2 }}</td>
                                    </tr>
                                    <tr class="table-success">
                                        <td><strong>Totale da pagare:</strong></td>
                                        <td class="text-right"><strong>€{{ fees.total_amount_euros|floatformat:2 }}</strong></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    
                    <!-- Azioni disponibili -->
                    <div class="card mb-3">
                        <div class="card-header">
                            <h6>⚡ Azioni Disponibili</h6>
                        </div>
                        <div class="card-body">
                            
                            <!-- SE LA RICHIESTA È PENDENTE -->
                            {% if purchase_request.status == 'pending' %}
                                {% if is_seller and can_approve %}
                                    <div class="alert alert-warning p-2 mb-3">
                                        <small><strong>⏳ Richiesta in attesa della tua approvazione</strong></small>
                                    </div>
                                    
                                    <div class="btn-group-vertical btn-group-block">
                                        <form method="post" action="{% url 'payments:process_request' purchase_request.uuid 'approve' %}" style="display:inline;">
                                            {% csrf_token %}
                                            <button type="submit" class="btn btn-success btn-block mb-2"
                                                    onclick="return confirm('✅ Approvare questa richiesta di acquisto?')">
                                                ✅ Approva Richiesta
                                            </button>
                                        </form>
                                        
                                        <form method="post" action="{% url 'payments:process_request' purchase_request.uuid 'reject' %}" style="display:inline;">
                                            {% csrf_token %}
                                            <button type="submit" class="btn btn-outline-danger btn-block"
                                                    onclick="return confirm('❌ Rifiutare questa richiesta di acquisto?')">
                                                ❌ Rifiuta
                                            </button>
                                        </form>
                                    </div>
                                    
                                {% elif is_buyer %}
                                    <div class="alert alert-info p-2 mb-3">
                                        <small><strong>⏳ In attesa di approvazione dal venditore</strong></small>
                                    </div>
                                    <p class="text-muted small">Il venditore {{ purchase_request.seller.username }} riceverà una notifica e potrà approvare o rifiutare la richiesta.</p>
                                {% endif %}
                            
                            <!-- SE LA RICHIESTA È APPROVATA -->
                            {% elif purchase_request.status == 'approved' %}
                                {% if is_buyer %}
                                    <div class="alert alert-success p-2 mb-3">
                                        <small><strong>✅ Richiesta approvata!</strong></small>
                                    </div>
                                    
                                    <!-- CONTROLLO TRANSAZIONE ESISTENTE -->
                                    {% if not purchase_request.payment_transaction %}
                                        <!-- NESSUNA TRANSAZIONE: MOSTRA PULSANTE PAGAMENTO -->
                                        <form method="post" action="{% url 'payments:create_checkout' purchase_request.uuid %}">
                                            {% csrf_token %}
                                            <button type="submit" class="btn btn-success btn-lg btn-block mb-3">
                                                💳 Procedi al Pagamento
                                                <br><small>€{{ fees.total_amount_euros|floatformat:2 }}</small>
                                            </button>
                                        </form>
                                        
                                        <div class="alert alert-info p-2">
                                            <small>
                                                <strong>🛡️ Pagamento Sicuro</strong><br>
                                                Sarai reindirizzato a Stripe per completare il pagamento in sicurezza.
                                            </small>
                                        </div>
                                        
                                    {% elif purchase_request.payment_transaction.status == 'pending' %}
                                        <!-- TRANSAZIONE CREATA MA NON PAGATA -->
                                        <div class="alert alert-warning p-2 mb-3">
                                            <small><strong>⏳ Transazione creata</strong><br>Completa il pagamento per finalizzare l'acquisto.</small>
                                        </div>
                                        
                                        <form method="post" action="{% url 'payments:create_checkout' purchase_request.uuid %}">
                                            {% csrf_token %}
                                            <button type="submit" class="btn btn-success btn-lg btn-block">
                                                💳 Completa Pagamento
                                                <br><small>€{{ fees.total_amount_euros|floatformat:2 }}</small>
                                            </button>
                                        </form>
                                        
                                    {% elif purchase_request.payment_transaction.status == 'processing' %}
                                        <!-- PAGAMENTO IN ELABORAZIONE -->
                                        <div class="alert alert-info p-2 mb-3">
                                            <small><strong>🔄 Pagamento in elaborazione</strong><br>Il pagamento è stato ricevuto ed è in elaborazione.</small>
                                        </div>
                                        
                                        <a href="{{ purchase_request.payment_transaction.get_absolute_url }}" class="btn btn-outline-info btn-block">
                                            👁️ Vedi Dettagli Transazione
                                        </a>
                                        
                                    {% elif purchase_request.payment_transaction.status == 'succeeded' %}
                                        <!-- PAGAMENTO COMPLETATO -->
                                        <div class="alert alert-success p-2 mb-3">
                                            <small><strong>🎉 Pagamento completato!</strong><br>L'acquisto è stato finalizzato con successo.</small>
                                        </div>
                                        
                                        <a href="{{ purchase_request.payment_transaction.get_absolute_url }}" class="btn btn-success btn-block">
                                            📄 Vedi Ricevuta
                                        </a>
                                    {% endif %}
                                    
                                {% elif is_seller %}
                                    <div class="alert alert-success p-2 mb-3">
                                        <small><strong>✅ Hai approvato questa richiesta</strong></small>
                                    </div>
                                    <p class="text-muted small">L'acquirente può ora procedere al pagamento.</p>
                                    
                                    {% if purchase_request.payment_transaction %}
                                        <a href="{{ purchase_request.payment_transaction.get_absolute_url }}" class="btn btn-outline-info btn-block">
                                            👁️ Stato Pagamento
                                        </a>
                                    {% endif %}
                                {% endif %}
                            
                            <!-- SE LA RICHIESTA È RIFIUTATA -->
                            {% elif purchase_request.status == 'rejected' %}
                                <div class="alert alert-danger p-2 mb-3">
                                    <small><strong>❌ Richiesta rifiutata</strong></small>
                                </div>
                                {% if is_buyer %}
                                    <p class="text-muted small">Il venditore ha rifiutato la richiesta. Puoi provare con un altro articolo.</p>
                                    <a href="{% url 'django_classified:index' %}" class="btn btn-primary btn-block">
                                        🔍 Cerca Altri Articoli
                                    </a>
                                {% endif %}
                            
                            <!-- SE LA RICHIESTA È COMPLETATA -->
                            {% elif purchase_request.status == 'completed' %}
                                <div class="alert alert-success p-2 mb-3">
                                    <small><strong>🎉 Acquisto completato!</strong></small>
                                </div>
                                

<<TRUNCATED FILE: limited to 300 lines>>
```


### templates/payments/request_purchase.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n widget_tweaks %}

{% block title %}Richiesta di Acquisto{% endblock %}

{% block body %}
<div class="container" style="max-width: 800px;">
    <h3>🛒 Richiesta di Acquisto</h3>
    
    <!-- Dettagli Articolo -->
    <div class="row mb-4">
        <div class="col-md-12">
            <div class="card">
                <div class="card-header bg-primary text-white">
                    <h5>📦 Articolo Selezionato</h5>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-4">
                            {% if item.image_set.first %}
                                <img src="{{ item.image_set.first.file.url }}" 
                                     alt="{{ item.title }}" 
                                     class="img-fluid rounded">
                            {% else %}
                                <div class="bg-light p-4 text-center rounded">
                                    <span class="text-muted">📷 Nessuna Immagine</span>
                                </div>
                            {% endif %}
                        </div>
                        <div class="col-md-8">
                            <h4>{{ item.title }}</h4>
                            <p><strong>Venditore:</strong> {{ item.user.username }}</p>
                            <p><strong>Prezzo:</strong> <span class="text-success">€{{ item.price|floatformat:0 }}</span></p>
                            {% if item.description %}
                                <p><strong>Descrizione:</strong></p>
                                <p class="text-muted">{{ item.description|truncatewords:30 }}</p>
                            {% endif %}
                            <a href="{{ item.get_absolute_url }}" class="btn btn-outline-info btn-sm" target="_blank">
                                👁️ Vedi Annuncio Completo
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Riepilogo Costi -->
    <div class="row mb-4">
        <div class="col-md-12">
            <div class="card border-warning">
                <div class="card-header bg-warning text-dark">
                    <h5>💰 Riepilogo Costi</h5>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-8">
                            <div class="d-flex justify-content-between mb-2">
                                <span>Prezzo articolo:</span>
                                <span>€{{ fees.item_price_cents|floatformat:2 }}</span>
                            </div>
                            <div class="d-flex justify-content-between mb-2">
                                <span>Commissione piattaforma (3%):</span>
                                <span>€{{ fees.platform_fee_cents|floatformat:2 }}</span>
                            </div>
                            <div class="d-flex justify-content-between mb-2">
                                <span>Commissione Stripe:</span>
                                <span>€{{ fees.stripe_fee_cents|floatformat:2 }}</span>
                            </div>
                            <hr>
                            <div class="d-flex justify-content-between">
                                <strong>Totale che pagherai:</strong>
                                <strong class="text-primary">€{{ total_euros|floatformat:2 }}</strong>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="alert alert-info">
                                <small>
                                    <strong>ℹ️ Commissioni:</strong><br>
                                    Le commissioni servono per mantenere la piattaforma sicura e garantire transazioni protette.
                                </small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Form Richiesta -->
    <div class="row mb-4">
        <div class="col-md-12">
            <div class="card">
                <div class="card-header">
                    <h5>📝 Dettagli della Richiesta</h5>
                </div>
                <div class="card-body">
                    <form method="post">
                        {% csrf_token %}
                        
                        <!-- Messaggio al venditore -->
                        <div class="form-group">
                            <label for="{{ form.message.id_for_label }}">💬 Messaggio al Venditore (opzionale):</label>
                            {{ form.message|add_class:"form-control" }}
                            {% if form.message.errors %}
                                <div class="text-danger">{{ form.message.errors }}</div>
                            {% endif %}
                            <small class="form-text text-muted">
                                Presentati e specifica eventuali domande sull'articolo
                            </small>
                        </div>

                        <!-- Metodo di consegna -->
                        <div class="form-group">
                            <label for="{{ form.delivery_method.id_for_label }}">🚚 Metodo di Consegna Preferito:</label>
                            {{ form.delivery_method|add_class:"form-control" }}
                            {% if form.delivery_method.errors %}
                                <div class="text-danger">{{ form.delivery_method.errors }}</div>
                            {% endif %}
                            <small class="form-text text-muted">Come preferisci ricevere l'articolo?</small>
                        </div>

                        <!-- Indirizzo di spedizione -->
                        <div class="form-group" id="shipping-address-group">
                            <label for="{{ form.shipping_address.id_for_label }}">📍 Indirizzo di Spedizione:</label>
                            {{ form.shipping_address|add_class:"form-control" }}
                            {% if form.shipping_address.errors %}
                                <div class="text-danger">{{ form.shipping_address.errors }}</div>
                            {% endif %}
                            <small class="form-text text-muted">
                                Necessario solo se scegli "Spedizione" o "Entrambi"
                            </small>
                        </div>

                        <!-- Processo di acquisto -->
                        <div class="alert alert-info">
                            <h6>ℹ️ Come Funziona il Processo</h6>
                            <ol>
                                <li><strong>Invii la richiesta</strong> al venditore con i tuoi dettagli</li>
                                <li><strong>Il venditore esamina</strong> la tua richiesta (può approvare o rifiutare)</li>
                                <li><strong>Se approvata:</strong> ricevi notifica e puoi procedere al pagamento</li>
                                <li><strong>Dopo il pagamento:</strong> coordinate consegna/ritiro con il venditore</li>
                            </ol>
                        </div>

                        <!-- Bottoni -->
                        <div class="text-center">
                            <button type="submit" class="btn btn-success btn-lg">
                                📤 Invia Richiesta di Acquisto
                            </button>
                            <a href="{{ item.get_absolute_url }}" class="btn btn-secondary btn-lg">
                                ❌ Annulla
                            </a>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Info Venditore -->
    {% if seller_profile %}
    <div class="row">
        <div class="col-md-12">
            <div class="card border-success">
                <div class="card-header bg-success text-white">
                    <h6>👤 Informazioni Venditore</h6>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-6">
                            <p><strong>Username:</strong> {{ item.user.username }}</p>
                            <p><strong>Accetta pagamenti:</strong> 
                                {% if seller_profile.accepts_payments %}
                                    <span class="badge badge-success">✅ Sì</span>
                                {% else %}
                                    <span class="badge badge-danger">❌ No</span>
                                {% endif %}
                            </p>
                        </div>
                        <div class="col-md-6">
                            {% if seller_profile.total_sales > 0 %}
                            <p><strong>Vendite completate:</strong> {{ seller_profile.total_sales }}</p>
                            <p><strong>Rating:</strong> 
                                {% if seller_profile.average_rating > 0 %}
                                    {{ seller_profile.average_rating|floatformat:1 }}/5 ⭐
                                {% else %}
                                    <span class="text-muted">Nessuna valutazione</span>
                                {% endif %}
                            </p>
                            {% else %}
                            <p class="text-muted">Nuovo venditore sulla piattaforma</p>
                            {% endif %}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {% endif %}
</div>

<script>
// Mostra/nascondi indirizzo basato sul metodo di consegna
document.addEventListener('DOMContentLoaded', function() {
    const deliveryMethod = document.getElementById('id_delivery_method');
    const shippingGroup = document.getElementById('shipping-address-group');
    
    function toggleShippingAddress() {
        const value = deliveryMethod.value;
        if (value === 'shipping' || value === 'both') {
            shippingGroup.style.display = 'block';
            document.getElementById('id_shipping_address').setAttribute('required', 'required');
        } else {
            shippingGroup.style.display = 'none';
            document.getElementById('id_shipping_address').removeAttribute('required');
        }
    }
    
    // Chiamata iniziale
    toggleShippingAddress();
    
    // Ascolta cambiamenti
    deliveryMethod.addEventListener('change', toggleShippingAddress);
});
</script>
{% endblock %}
```


### templates/payments/sales_history.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n %}

{% block title %}Le Mie Vendite{% endblock %}

{% block body %}
<div class="container">
    <h3>💸 Le Mie Vendite</h3>
    
    {% if transactions %}
        <!-- Statistiche Vendite -->
        <div class="row mb-4">
            <div class="col-md-3">
                <div class="card bg-success text-white">
                    <div class="card-body text-center">
                        <h4>{{ transactions|length }}</h4>
                        <p class="mb-0">Vendite Totali</p>
                    </div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card bg-info text-white">
                    <div class="card-body text-center">
                        <h4>{{ transactions|dictsort:"status"|dictsortreversed:"succeeded"|length }}</h4>
                        <p class="mb-0">Completate</p>
                    </div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card bg-warning text-white">
                    <div class="card-body text-center">
                        <h4>€0.00</h4>
                        <p class="mb-0">Ricavi Netti*</p>
                    </div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card bg-primary text-white">
                    <div class="card-body text-center">
                        <h4>⭐ 5.0</h4>
                        <p class="mb-0">Rating Medio</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Lista Vendite -->
        <div class="card">
            <div class="card-header">
                <h5>📋 Cronologia Vendite</h5>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>Data</th>
                                <th>Articolo</th>
                                <th>Acquirente</th>
                                <th>Importi</th>
                                <th>Stato</th>
                                <th>Azioni</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for transaction in transactions %}
                            <tr>
                                <td>{{ transaction.created_at|date:"d/m/Y H:i" }}</td>
                                <td>
                                    <div class="d-flex align-items-center">
                                        {% if transaction.item.image_set.first %}
                                            <img src="{{ transaction.item.image_set.first.file.url }}" 
                                                 alt="{{ transaction.item.title }}" 
                                                 class="mr-2 rounded" style="width: 40px; height: 40px; object-fit: cover;">
                                        {% endif %}
                                        <div>
                                            <strong>{{ transaction.item.title|truncatechars:25 }}</strong>
                                        </div>
                                    </div>
                                </td>
                                <td>
                                    <strong>{{ transaction.buyer.username }}</strong>
                                    <br><small class="text-muted">{{ transaction.buyer_email }}</small>
                                </td>
                                <td>
                                    <strong>€{{ transaction.item_price_euros|floatformat:2 }}</strong>
                                    <br><small class="text-muted">
                                        Totale pagato: €{{ transaction.total_amount_euros|floatformat:2 }}<br>
                                        <span class="text-danger">Commissioni: -€{{ transaction.platform_fee_euros|add:transaction.stripe_fee_euros|floatformat:2 }}</span>
                                    </small>
                                </td>
                                <td>
                                    {% if transaction.status == 'pending' %}
                                        <span class="badge badge-warning">⏳ In Attesa</span>
                                    {% elif transaction.status == 'processing' %}
                                        <span class="badge badge-info">🔄 In Elaborazione</span>
                                    {% elif transaction.status == 'succeeded' %}
                                        <span class="badge badge-success">✅ Completata</span>
                                    {% elif transaction.status == 'failed' %}
                                        <span class="badge badge-danger">❌ Fallita</span>
                                    {% elif transaction.status == 'cancelled' %}
                                        <span class="badge badge-secondary">🚫 Annullata</span>
                                    {% elif transaction.status == 'refunded' %}
                                        <span class="badge badge-warning">💸 Rimborsata</span>
                                    {% endif %}
                                    
                                    {% if transaction.completed_at %}
                                        <br><small class="text-muted">{{ transaction.completed_at|date:"d/m/Y" }}</small>
                                    {% endif %}
                                </td>
                                <td>
                                    <div class="btn-group-vertical btn-group-sm">
                                        <a href="{{ transaction.get_absolute_url }}" class="btn btn-outline-info btn-sm">
                                            👁️ Dettagli
                                        </a>
                                        
                                        {% if transaction.shipping_address %}
                                            <button class="btn btn-outline-warning btn-sm" 
                                                    title="Spedire a: {{ transaction.shipping_address|truncatechars:50 }}"
                                                    data-toggle="tooltip">
                                                📦 Spedizione
                                            </button>
                                        {% endif %}
                                        
                                        {% if transaction.status == 'succeeded' %}
                                            <a href="mailto:{{ transaction.buyer_email }}" class="btn btn-outline-primary btn-sm">
                                                ✉️ Contatta
                                            </a>
                                        {% endif %}
                                    </div>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

    {% else %}
        <!-- Stato Vuoto -->
        <div class="jumbotron text-center">
            <h4>💸 Nessuna Vendita Ancora</h4>
            <p class="lead">Non hai ancora ricevuto pagamenti per i tuoi annunci.</p>
            <hr class="my-4">
            <p>Inizia a vendere attivando i pagamenti nei tuoi annunci!</p>
            <div class="btn-group">
                <a class="btn btn-success btn-lg" href="{% url 'payments:seller_setup' %}">⚙️ Configura Vendite</a>
                <a class="btn btn-primary btn-lg" href="{% url 'django_classified:item-new' %}">📝 Nuovo Annuncio</a>
            </div>
        </div>
    {% endif %}

    <!-- Sezione Consigli per Venditori -->
    <div class="card mt-4 border-success">
        <div class="card-header bg-success text-white">
            <h6>💡 Consigli per Vendere Meglio</h6>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-md-6">
                    <h6>📸 Foto di Qualità</h6>
                    <p class="small text-muted">Usa foto chiare e ben illuminate per attirare più acquirenti</p>
                    
                    <h6>📝 Descrizioni Dettagliate</h6>
                    <p class="small text-muted">Descrivi accuratamente condizioni e dettagli dell'articolo</p>
                </div>
                <div class="col-md-6">
                    <h6>⚡ Risposte Rapide</h6>
                    <p class="small text-muted">Rispondi velocemente alle richieste di acquisto</p>
                    
                    <h6>📦 Spedizioni Veloci</h6>
                    <p class="small text-muted">Spedisci entro 1-2 giorni lavorativi per ottenere feedback positivi</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Commissioni Info -->
    <div class="alert alert-warning mt-4">
        <h6>💰 Informazioni Commissioni</h6>
        <p class="mb-0">
            <strong>Commissione Piattaforma:</strong> 3% del prezzo dell'articolo<br>
            <strong>Commissione Stripe:</strong> 1.4% + €0.25 per transazione<br>
            <small class="text-muted">Le commissioni vengono detratte automaticamente dal pagamento dell'acquirente prima del trasferimento</small>
        </p>
    </div>

    <!-- Link navigazione -->
    <div class="text-center mt-4">
        <a href="{% url 'django_classified:index' %}" class="btn btn-secondary">🏠 Torna alla Home</a>
        <a href="{% url 'payments:purchase_history' %}" class="btn btn-outline-info">🛍️ I Miei Acquisti</a>
        <a href="{% url 'payments:seller_setup' %}" class="btn btn-outline-success">⚙️ Configurazione</a>
    </div>
</div>

<!-- Script per tooltip -->
<script>
$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})
</script>
{% endblock %}
```


### templates/payments/seller_requests.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n %}

{% block title %}Richieste di Acquisto Ricevute{% endblock %}

{% block body %}
<div class="container">
    <div class="row">
        <div class="col-md-12">
            <h3>🏪 Richieste di Acquisto Ricevute</h3>
            
            {% if pending_count > 0 %}
                <div class="alert alert-warning">
                    <strong>⚠️ {{ pending_count }} richiesta{{ pending_count|pluralize:"," }} in attesa di approvazione</strong>
                </div>
            {% endif %}
            
            {% if requests %}
                {% for request in requests %}
                <div class="card mb-4 {% if request.status == 'pending' %}border-warning{% elif request.status == 'approved' %}border-success{% elif request.status == 'rejected' %}border-danger{% elif request.status == 'expired' %}border-secondary{% endif %}">
                    
                    <!-- Header con stato -->
                    <div class="card-header {% if request.status == 'pending' %}bg-warning{% elif request.status == 'approved' %}bg-success text-white{% elif request.status == 'rejected' %}bg-danger text-white{% elif request.status == 'expired' %}bg-secondary text-white{% endif %}">
                        <div class="row">
                            <div class="col-md-8">
                                <h5 class="mb-1">
                                    {% if request.status == 'pending' %}⏳{% elif request.status == 'approved' %}✅{% elif request.status == 'rejected' %}❌{% elif request.status == 'expired' %}⌛{% endif %}
                                    {{ request.item.title }}
                                </h5>
                                <small>
                                    Richiesta #{{ request.uuid.hex|slice:":8" }} • 
                                    {{ request.created|date:"d/m/Y H:i" }}
                                    {% if request.expires_at %}
                                        • Scade: {{ request.expires_at|date:"d/m/Y H:i" }}
                                    {% endif %}
                                </small>
                            </div>
                            <div class="col-md-4 text-right">
                                <span class="badge badge-{% if request.status == 'pending' %}warning{% elif request.status == 'approved' %}success{% elif request.status == 'rejected' %}danger{% else %}secondary{% endif %} badge-lg">
                                    {{ request.get_status_display }}
                                </span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="card-body">
                        <div class="row">
                            <!-- Dettagli acquirente -->
                            <div class="col-md-4">
                                <h6>🛒 Acquirente</h6>
                                <p class="mb-1"><strong>{{ request.buyer.username }}</strong></p>
                                <p class="mb-1">📧 {{ request.buyer.email }}</p>
                                
                                {% if request.buyer.seller_profile %}
                                    <small class="text-muted">
                                        {% if request.buyer.seller_profile.total_sales > 0 %}
                                            ⭐ {{ request.buyer.seller_profile.average_rating|floatformat:1 }}/5
                                            ({{ request.buyer.seller_profile.total_sales }} vendite)
                                        {% else %}
                                            👤 Nuovo utente
                                        {% endif %}
                                    </small>
                                {% endif %}
                            </div>
                            
                            <!-- Dettagli prodotto e consegna -->
                            <div class="col-md-4">
                                <h6>📦 Articolo e Consegna</h6>
                                <p class="mb-1"><strong>💰 €{{ request.item.price }}</strong></p>
                                <p class="mb-1">
                                    🚚 {{ request.get_delivery_method_display }}
                                </p>
                                
                                {% if request.shipping_address %}
                                    <div class="alert alert-light p-2 mt-2">
                                        <small><strong>📍 Indirizzo:</strong><br>{{ request.shipping_address }}</small>
                                    </div>
                                {% endif %}
                            </div>
                            
                            <!-- Importi -->
                            <div class="col-md-4">
                                <h6>💳 Riepilogo Importi</h6>
                                <div class="table-sm">
                                    {% with fees=request.item.price|floatformat:2 %}
                                        <small>
                                            Prezzo: €{{ request.item.price }}<br>
                                            + Commissioni: ~€{{ fees|add:"0"|floatformat:2 }}<br>
                                            <strong>Totale acquirente: ~€{{ request.item.price|add:fees|floatformat:2 }}</strong><br>
                                            <em class="text-muted">Netto a te: €{{ request.item.price }}</em>
                                        </small>
                                    {% endwith %}
                                </div>
                            </div>
                        </div>
                        
                        <!-- Messaggio dell'acquirente -->
                        {% if request.message %}
                        <div class="row mt-3">
                            <div class="col-md-12">
                                <div class="alert alert-info">
                                    <h6>💬 Messaggio dell'acquirente:</h6>
                                    <p class="mb-0">{{ request.message|linebreaks }}</p>
                                </div>
                            </div>
                        </div>
                        {% endif %}
                        
                        <!-- Azioni disponibili -->
                        <div class="row mt-3">
                            <div class="col-md-12">
                                {% if request.status == 'pending' and not request.is_expired %}
                                    <div class="btn-group" role="group">
                                        <form method="post" action="{% url 'payments:process_request' request.uuid 'approve' %}" style="display:inline;" 
                                              onsubmit="return confirm('✅ Approvare questa richiesta di acquisto?\n\nL\'acquirente potrà procedere al pagamento.')">
                                            {% csrf_token %}
                                            <button type="submit" class="btn btn-success">
                                                ✅ Approva Richiesta
                                            </button>
                                        </form>
                                        
                                        <form method="post" action="{% url 'payments:process_request' request.uuid 'reject' %}" style="display:inline;"
                                              onsubmit="return confirm('❌ Rifiutare questa richiesta di acquisto?\n\nL\'acquirente riceverà una notifica.')">
                                            {% csrf_token %}
                                            <button type="submit" class="btn btn-outline-danger">
                                                ❌ Rifiuta
                                            </button>
                                        </form>
                                    </div>
                                    
                                {% elif request.status == 'approved' %}
                                    <div class="alert alert-success">
                                        <strong>✅ Richiesta Approvata</strong>
                                        <p class="mb-1">L'acquirente può ora procedere al pagamento.</p>
                                        {% if request.payment_transaction %}
                                            <p class="mb-0">
                                                <a href="{% url 'payments:request_detail' request.uuid %}" class="btn btn-sm btn-outline-success">
                                                    👁️ Vedi Stato Pagamento
                                                </a>
                                            </p>
                                        {% endif %}
                                    </div>
                                    
                                {% elif request.status == 'rejected' %}
                                    <div class="alert alert-danger">
                                        <strong>❌ Richiesta Rifiutata</strong>
                                    </div>
                                    
                                {% elif request.is_expired %}
                                    <div class="alert alert-secondary">
                                        <strong>⌛ Richiesta Scaduta</strong>
                                        <p class="mb-0">Questa richiesta è scaduta automaticamente.</p>
                                    </div>
                                {% endif %}
                                
                                <!-- Link dettaglio -->
                                <a href="{% url 'payments:request_detail' request.uuid %}" class="btn btn-outline-info btn-sm ml-2">
                                    👁️ Vedi Dettagli Completi
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                {% endfor %}
                
                <!-- Paginazione -->
                {% if is_paginated %}
                <nav aria-label="Paginazione richieste">
                    <ul class="pagination justify-content-center">
                        {% if page_obj.has_previous %}
                            <li class="page-item">
                                <a class="page-link" href="?page={{ page_obj.previous_page_number }}">&laquo; Precedente</a>
                            </li>
                        {% endif %}
                        
                        <li class="page-item active">
                            <span class="page-link">Pagina {{ page_obj.number }} di {{ page_obj.paginator.num_pages }}</span>
                        </li>
                        
                        {% if page_obj.has_next %}
                            <li class="page-item">
                                <a class="page-link" href="?page={{ page_obj.next_page_number }}">Successiva &raquo;</a>
                            </li>
                        {% endif %}
                    </ul>
                </nav>
                {% endif %}
                
            {% else %}
                <!-- Nessuna richiesta -->
                <div class="jumbotron text-center">
                    <h4>📭 Nessuna Richiesta di Acquisto</h4>
                    <p class="lead">Non hai ancora ricevuto richieste di acquisto per i tuoi annunci.</p>
                    
                    <hr class="my-4">
                    
                    <div class="row justify-content-center">
                        <div class="col-md-8">
                            <h6>💡 Suggerimenti per ricevere più richieste:</h6>
                            <ul class="text-left">
                                <li><strong>Prezzi competitivi:</strong> Confronta i tuoi prezzi con annunci simili</li>
                                <li><strong>Foto di qualità:</strong> Aggiungi immagini chiare dei tuoi articoli</li>
                                <li><strong>Descrizioni dettagliate:</strong> Spiega le condizioni del prodotto</li>
                                <li><strong>Pagamenti online:</strong> Facilita gli acquisti abilitando Stripe</li>
                            </ul>
                        </div>
                    </div>
                    
                    <a class="btn btn-primary btn-lg" href="{% url 'django_classified:user-items' %}" role="button">
                        📝 Gestisci i Tuoi Annunci
                    </a>
                </div>
            {% endif %}
        </div>
    </div>
</div>

<!-- Script per funzionalità aggiuntive -->
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Auto-refresh per richieste pendenti
    const pendingCount = {{ pending_count|default:0 }};
    if (pendingCount > 0) {
        // Refresh ogni 2 minuti se ci sono richieste pendenti
        setTimeout(function() {
            window.location.reload();
        }, 120000);
    }
    
    // Suoni di notifica (opzionale)
    if (pendingCount > 0 && 'Notification' in window) {
        // Chiedi permesso notifiche
        Notification.requestPermission();
    }
});
</script>
{% endblock %}
```


### templates/payments/seller_setup.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n widget_tweaks %}

{% block title %}Impostazioni Venditore{% endblock %}

{% block body %}
<div class="container" style="max-width: 700px;">
    <h3>⚙️ Impostazioni Venditore</h3>
    
    {% if is_new_seller %}
        <div class="alert alert-info">
            <h5>👋 Benvenuto come Venditore!</h5>
            <p class="mb-0">Configura le tue preferenze per iniziare a vendere su NINVENDO.</p>
        </div>
    {% endif %}
    
    <div class="card">
        <div class="card-header bg-primary text-white">
            <h5>💰 Configurazione Vendite</h5>
        </div>
        <div class="card-body">
            <form method="post">
                {% csrf_token %}
                
                <!-- Accetta pagamenti -->
                <div class="form-group">
                    <div class="form-check">
                        {{ form.accepts_payments|add_class:"form-check-input" }}
                        <label class="form-check-label" for="{{ form.accepts_payments.id_for_label }}">
                            <strong>💳 Accetta pagamenti online</strong>
                        </label>
                    </div>
                    <small class="form-text text-muted">
                        Permetti agli utenti di acquistare i tuoi annunci con carte di credito/debito tramite Stripe
                    </small>
                    {% if form.accepts_payments.errors %}
                        <div class="text-danger">{{ form.accepts_payments.errors }}</div>
                    {% endif %}
                </div>

                <hr>

                <!-- Auto-approvazione -->
                <div class="form-group">
                    <div class="form-check">
                        {{ form.auto_accept_payments|add_class:"form-check-input" }}
                        <label class="form-check-label" for="{{ form.auto_accept_payments.id_for_label }}">
                            <strong>⚡ Approva automaticamente le richieste</strong>
                        </label>
                    </div>
                    <small class="form-text text-muted">
                        Le richieste di acquisto saranno approvate automaticamente senza la tua conferma manuale
                    </small>
                    <div class="alert alert-warning mt-2">
                        <small>
                            <strong>⚠️ Attenzione:</strong> Sconsigliato per articoli di valore elevato. 
                            Con l'approvazione automatica gli acquirenti potranno procedere immediatamente al pagamento.
                        </small>
                    </div>
                    {% if form.auto_accept_payments.errors %}
                        <div class="text-danger">{{ form.auto_accept_payments.errors }}</div>
                    {% endif %}
                </div>

                <hr>

                <!-- Commissioni info -->
                <div class="alert alert-light">
                    <h6>📊 Sistema Commissioni</h6>
                    <p class="mb-2">Su ogni vendita vengono applicate automaticamente:</p>
                    <ul class="mb-2">
                        <li><strong>3% di commissione piattaforma NINVENDO</strong></li>
                        <li><strong>1.4% + €0.25 di commissione Stripe</strong> (processore pagamenti)</li>
                    </ul>
                    <p class="mb-0 small text-muted">
                        Le commissioni sono a carico dell'acquirente e vengono aggiunte automaticamente al prezzo finale.
                        Tu riceverai esattamente l'importo pubblicato nel tuo annuncio.
                    </p>
                </div>

                <!-- Pulsanti -->
                <div class="text-center">
                    <button type="submit" class="btn btn-success btn-lg">
                        💾 Salva Configurazione
                    </button>
                    <a href="{% url 'django_classified:index' %}" class="btn btn-secondary btn-lg ml-2">
                        ↩️ Torna alla Home
                    </a>
                </div>
            </form>
        </div>
    </div>

    <!-- Statistiche (se esistenti) -->
    {% if profile.total_sales > 0 %}
        <div class="card mt-4">
            <div class="card-header bg-success text-white">
                <h5>📈 Le Tue Statistiche</h5>
            </div>
            <div class="card-body">
                <div class="row text-center">
                    <div class="col-md-4">
                        <h4 class="text-primary">{{ profile.total_sales }}</h4>
                        <p class="text-muted">Rating Medio</p>
                    </div>
                </div>
            </div>
        </div>
    {% endif %}

    <!-- Link utili -->
    <div class="card mt-4">
        <div class="card-header">
            <h6>🔗 Link Utili</h6>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-md-6">
                    <h6>📊 Gestione Vendite</h6>
                    <ul class="list-unstyled">
                        <li><a href="{% url 'payments:sales_history' %}">💸 Cronologia Vendite</a></li>
                        <li><a href="{% url 'django_classified:user-items' %}">📝 I Miei Annunci</a></li>
                        <li><a href="{% url 'django_classified:item-new' %}">➕ Nuovo Annuncio</a></li>
                    </ul>
                </div>
                <div class="col-md-6">
                    <h6>🔄 Sistema Scambi</h6>
                    <ul class="list-unstyled">
                        <li><a href="{% url 'trade:inbox' %}">📥 Scambi Ricevuti</a></li>
                        <li><a href="{% url 'trade:sent' %}">📤 Scambi Inviati</a></li>
                        <li><a href="{% url 'trade:profile' %}">👤 Profilo Scambi</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- FAQ -->
    <div class="card mt-4">
        <div class="card-header">
            <h6>❓ Domande Frequenti</h6>
        </div>
        <div class="card-body">
            <div class="accordion" id="faqAccordion">
                
                <div class="card">
                    <div class="card-header" id="faq1">
                        <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#answer1">
                            <strong>Come funzionano i pagamenti?</strong>
                        </button>
                    </div>
                    <div id="answer1" class="collapse" data-parent="#faqAccordion">
                        <div class="card-body">
                            <p>I pagamenti sono gestiti tramite <strong>Stripe</strong>, uno dei sistemi più sicuri al mondo:</p>
                            <ol>
                                <li>L'acquirente invia una richiesta</li>
                                <li>Tu approvi (manualmente o automaticamente)</li>
                                <li>L'acquirente paga con carta di credito/debito</li>
                                <li>Tu ricevi il pagamento direttamente sul tuo conto</li>
                            </ol>
                        </div>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-header" id="faq2">
                        <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#answer2">
                            <strong>Quando ricevo i soldi?</strong>
                        </button>
                    </div>
                    <div id="answer2" class="collapse" data-parent="#faqAccordion">
                        <div class="card-body">
                            <p>I pagamenti vengono trasferiti automaticamente sul tuo conto corrente entro <strong>2-7 giorni lavorativi</strong> dal completamento della transazione, secondo le tempistiche standard di Stripe.</p>
                        </div>
                    </div>
                </div>
                
                <div class="card">
                    <div class="card-header" id="faq3">
                        <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#answer3">
                            <strong>Posso ancora fare scambi gratuiti?</strong>
                        </button>
                    </div>
                    <div id="answer3" class="collapse" data-parent="#faqAccordion">
                        <div class="card-body">
                            <p><strong>Assolutamente sì!</strong> Il sistema di baratto rimane completamente gratuito e disponibile per tutti gli utenti, indipendentemente dalle impostazioni di pagamento.</p>
                        </div>
                    </div>
                </div>
                
            </div>
        </div>
    </div>
</div>
{% endblock %}="text-muted">Vendite Completate</p>
                    </div>
                    <div class="col-md-4">
                        <h4 class="text-success">€{{ profile.total_revenue_euros|floatformat:2 }}</h4>
                        <p class="text-muted">Ricavi Totali</p>
                    </div>
                    <div class="col-md-4">
                        <h4 class="text-warning">{{ profile.average_rating|floatformat:1 }}⭐</h4>
                        <p class
```


### templates/payments/template_seller_setup.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n %}

{% block title %}Impostazioni Vendite{% endblock %}

{% block body %}
<div class="container" style="max-width: 800px;">
    <h3>⚙️ Impostazioni Venditore</h3>
    
    <!-- Stato Configurazione -->
    <div class="row mb-4">
        <div class="col-md-12">
            <div class="card">
                <div class="card-header bg-info text-white">
                    <h5>📊 Stato del Tuo Profilo Venditore</h5>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-6">
                            <h6>✅ Configurazione Base</h6>
                            <p class="text-success mb-1">
                                <strong>Account attivo</strong> - Puoi ricevere richieste di acquisto
                            </p>
                            <small class="text-muted">Profilo creato: {{ profile.created_at|date:"d/m/Y" }}</small>
                        </div>
                        <div class="col-md-6">
                            <h6>📈 Statistiche</h6>
                            <p class="mb-1">
                                <strong>{{ profile.total_sales }}</strong> vendite completate<br>
                                <strong>€{{ profile.total_revenue_euros|floatformat:2 }}</strong> ricavi totali<br>
                                <strong>⭐ {{ profile.average_rating|floatformat:1 }}/5</strong> rating medio
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Form Configurazione -->
    <div class="card">
        <div class="card-header">
            <h5>🛠️ Configurazione</h5>
        </div>
        <div class="card-body">
            <form method="post">
                {% csrf_token %}
                
                <!-- Sistema Pagamenti -->
                <div class="form-group">
                    <div class="form-check">
                        {{ form.accepts_payments }}
                        <label class="form-check-label" for="{{ form.accepts_payments.id_for_label }}">
                            <strong>{{ form.accepts_payments.label }}</strong>
                        </label>
                    </div>
                    <small class="form-text text-muted">{{ form.accepts_payments.help_text }}</small>
                    {% if form.accepts_payments.errors %}
                        <div class="text-danger">{{ form.accepts_payments.errors }}</div>
                    {% endif %}
                </div>

                <div class="form-group">
                    <div class="form-check">
                        {{ form.auto_accept_payments }}
                        <label class="form-check-label" for="{{ form.auto_accept_payments.id_for_label }}">
                            <strong>{{ form.auto_accept_payments.label }}</strong>
                        </label>
                    </div>
                    <small class="form-text text-muted">{{ form.auto_accept_payments.help_text }}</small>
                    {% if form.auto_accept_payments.errors %}
                        <div class="text-danger">{{ form.auto_accept_payments.errors }}</div>
                    {% endif %}
                </div>

                <!-- Informazioni Commissioni -->
                <div class="alert alert-warning">
                    <h6>💰 Schema Commissioni</h6>
                    <div class="row">
                        <div class="col-md-6">
                            <p class="mb-1"><strong>Commissione Piattaforma:</strong></p>
                            <p class="text-danger">3% del prezzo dell'articolo</p>
                        </div>
                        <div class="col-md-6">
                            <p class="mb-1"><strong>Commissione Stripe:</strong></p>
                            <p class="text-danger">1.4% + €0.25 per transazione</p>
                        </div>
                    </div>
                    <hr>
                    <h6>Esempio Calcolo:</h6>
                    <div class="table-responsive">
                        <table class="table table-sm">
                            <tr>
                                <td>Prezzo articolo</td>
                                <td class="text-right">€50.00</td>
                            </tr>
                            <tr class="text-danger">
                                <td>Commissione piattaforma (3%)</td>
                                <td class="text-right">-€1.50</td>
                            </tr>
                            <tr class="text-danger">
                                <td>Commissione Stripe (1.4% + €0.25)</td>
                                <td class="text-right">-€0.95</td>
                            </tr>
                            <tr class="font-weight-bold">
                                <td>Totale pagato dall'acquirente</td>
                                <td class="text-right">€52.45</td>
                            </tr>
                            <tr class="text-success font-weight-bold">
                                <td>Tu ricevi</td>
                                <td class="text-right">€50.00</td>
                            </tr>
                        </table>
                    </div>
                    <small class="text-muted">
                        Le commissioni sono a carico dell'acquirente e vengono aggiunte al prezzo dell'articolo
                    </small>
                </div>

                <!-- Come Funziona -->
                <div class="card mb-3">
                    <div class="card-header">
                        <h6>❓ Come Funziona il Sistema di Pagamenti</h6>
                    </div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-6">
                                <h6>1. 📝 Richiesta di Acquisto</h6>
                                <p class="small text-muted">L'acquirente invia una richiesta per il tuo annuncio con messaggio e dettagli di consegna</p>
                                
                                <h6>2. ✅ Approvazione</h6>
                                <p class="small text-muted">Tu approvi o rifiuti la richiesta (automatico se abilitato)</p>
                            </div>
                            <div class="col-md-6">
                                <h6>3. 💳 Pagamento</h6>
                                <p class="small text-muted">L'acquirente paga con carta tramite Stripe (sicuro e crittografato)</p>
                                
                                <h6>4. 📦 Consegna</h6>
                                <p class="small text-muted">Spedisci l'articolo o organizza il ritiro secondo gli accordi</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Stripe Setup (Solo per info, non funzionale senza account) -->
                <div class="alert alert-info">
                    <h6>🔧 Configurazione Stripe</h6>
                    <p>
                        <strong>Stato:</strong> 
                        {% if profile.stripe_onboarding_completed %}
                            <span class="text-success">✅ Completata</span>
                        {% else %}
                            <span class="text-warning">⚠️ Non configurata</span>
                        {% endif %}
                    </p>
                    {% if not profile.stripe_onboarding_completed %}
                        <p class="mb-2">Per ricevere pagamenti devi completare la configurazione Stripe:</p>
                        <button type="button" class="btn btn-warning" disabled>
                            🔗 Completa Configurazione Stripe (Demo Mode)
                        </button>
                        <br><small class="text-muted">In modalità demo - sarà attivato quando avrai un account Stripe reale</small>
                    {% endif %}
                </div>

                <!-- Pulsanti Azione -->
                <div class="text-center">
                    <button type="submit" class="btn btn-success btn-lg">
                        💾 Salva Configurazione
                    </button>
                    <a href="{% url 'django_classified:index' %}" class="btn btn-secondary btn-lg ml-2">
                        🏠 Torna alla Home
                    </a>
                </div>
            </form>
        </div>
    </div
```


### templates/payments/transaction_detail.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n %}

{% block title %}Transazione #{{ transaction.uuid.hex|slice:":8" }}{% endblock %}

{% block body %}
<div class="container">
    <div class="row">
        <div class="col-md-12">
            <h3>💳 Dettagli Transazione #{{ transaction.uuid.hex|slice:":8" }}</h3>
            
            <!-- Status della transazione -->
            <div class="alert 
                {% if transaction.status == 'pending' %}alert-warning
                {% elif transaction.status == 'processing' %}alert-info
                {% elif transaction.status == 'succeeded' %}alert-success
                {% elif transaction.status == 'failed' %}alert-danger
                {% elif transaction.status == 'cancelled' %}alert-secondary
                {% elif transaction.status == 'refunded' %}alert-warning
                {% endif %}">
                <div class="row">
                    <div class="col-md-8">
                        <h4>
                            {% if transaction.status == 'pending' %}⏳ In Attesa
                            {% elif transaction.status == 'processing' %}🔄 In Elaborazione
                            {% elif transaction.status == 'succeeded' %}✅ Completata
                            {% elif transaction.status == 'failed' %}❌ Fallita
                            {% elif transaction.status == 'cancelled' %}🚫 Annullata
                            {% elif transaction.status == 'refunded' %}💸 Rimborsata
                            {% endif %}
                        </h4>
                        <p class="mb-0">{{ transaction.get_status_display }}</p>
                    </div>
                    <div class="col-md-4 text-right">
                        <p class="mb-1"><strong>Creata:</strong> {{ transaction.created_at|date:"d/m/Y H:i" }}</p>
                        {% if transaction.completed_at %}
                            <p class="mb-0"><strong>Completata:</strong> {{ transaction.completed_at|date:"d/m/Y H:i" }}</p>
                        {% endif %}
                    </div>
                </div>
            </div>
            
            <div class="row">
                <!-- Dettagli transazione -->
                <div class="col-md-8">
                    <!-- Informazioni articolo -->
                    <div class="card mb-4">
                        <div class="card-header">
                            <h5>🎮 Articolo Acquistato</h5>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-md-3">
                                    {% if transaction.item.image_set.first %}
                                        <img src="{{ transaction.item.image_set.first.file.url }}" 
                                             alt="{{ transaction.item.title }}" 
                                             class="img-fluid rounded">
                                    {% else %}
                                        <div class="bg-light p-3 text-center rounded">
                                            <span class="text-muted">Nessuna immagine</span>
                                        </div>
                                    {% endif %}
                                </div>
                                <div class="col-md-9">
                                    <h6>{{ transaction.item.title }}</h6>
                                    <p class="text-muted">{{ transaction.item.description|truncatewords:20 }}</p>
                                    <p>
                                        <a href="{{ transaction.item.get_absolute_url }}" 
                                           class="btn btn-outline-primary btn-sm">
                                            👁️ Vedi Annuncio
                                        </a>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Informazioni partecipanti -->
                    <div class="row">
                        <!-- Acquirente -->
                        <div class="col-md-6">
                            <div class="card mb-3 {% if is_buyer %}border-primary{% endif %}">
                                <div class="card-header {% if is_buyer %}bg-primary text-white{% endif %}">
                                    <h6>🛒 Acquirente</h6>
                                </div>
                                <div class="card-body">
                                    <p><strong>{{ transaction.buyer.username }}</strong>
                                        {% if is_buyer %}<span class="badge badge-primary ml-2">Tu</span>{% endif %}
                                    </p>
                                    <p>📧 {{ transaction.buyer_email }}</p>
                                    {% if transaction.buyer_name %}
                                        <p>👤 {{ transaction.buyer_name }}</p>
                                    {% endif %}
                                </div>
                            </div>
                        </div>
                        
                        <!-- Venditore -->
                        <div class="col-md-6">
                            <div class="card mb-3 {% if is_seller %}border-success{% endif %}">
                                <div class="card-header {% if is_seller %}bg-success text-white{% endif %}">
                                    <h6>🏪 Venditore</h6>
                                </div>
                                <div class="card-body">
                                    <p><strong>{{ transaction.seller.username }}</strong>
                                        {% if is_seller %}<span class="badge badge-success ml-2">Tu</span>{% endif %}
                                    </p>
                                    {% if transaction.seller.seller_profile %}
                                        <p>📊 {{ transaction.seller.seller_profile.total_sales }} vendite</p>
                                        <p>⭐ {{ transaction.seller.seller_profile.average_rating|floatformat:1 }}/5</p>
                                    {% endif %}
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Indirizzo di spedizione -->
                    {% if transaction.shipping_address %}
                    <div class="card mb-3">
                        <div class="card-header">
                            <h6>📍 Indirizzo di Spedizione</h6>
                        </div>
                        <div class="card-body">
                            <address>{{ transaction.shipping_address|linebreaks }}</address>
                        </div>
                    </div>
                    {% endif %}
                    
                    <!-- Note -->
                    {% if transaction.notes %}
                    <div class="card mb-3">
                        <div class="card-header">
                            <h6>📝 Note</h6>
                        </div>
                        <div class="card-body">
                            {{ transaction.notes|linebreaks }}
                        </div>
                    </div>
                    {% endif %}
                </div>
                
                <!-- Sidebar - Importi e azioni -->
                <div class="col-md-4">
                    <!-- Riepilogo importi -->
                    <div class="card mb-3">
                        <div class="card-header">
                            <h6>💰 Riepilogo Importi</h6>
                        </div>
                        <div class="card-body">
                            <table class="table table-sm">
                                <tbody>
                                    <tr>
                                        <td>Prezzo articolo:</td>
                                        <td class="text-right"><strong>€{{ transaction.item_price_euros }}</strong></td>
                                    </tr>
                                    <tr>
                                        <td>Commissione piattaforma:</td>
                                        <td class="text-right">€{{ transaction.platform_fee_euros }}</td>
                                    </tr>
                                    <tr>
                                        <td>Commissione Stripe:</td>
                                        <td class="text-right">€{{ transaction.stripe_fee_euros }}</td>
                                    </tr>
                                    <tr class="table-success">
                                        <td><strong>Totale pagato:</strong></td>
                                        <td class="text-right"><strong>€{{ transaction.total_amount_euros }}</strong></td>
                                    </tr>
                                </tbody>
                            </table>
                            
                            {% if is_seller %}
                                <div class="alert alert-info p-2">
                                    <small>
                                        <strong>💰 Il tuo ricavo:</strong><br>
                                        €{{ transaction.item_price_euros }}
                                        <br><em>(commissioni detratte automaticamente)</em>
                                    </small>
                                </div>
                            {% endif %}
                        </div>
                    </div>
                    
                    <!-- Azioni disponibili -->
                    <div class="card mb-3">
                        <div class="card-header">
                            <h6>⚡ Azioni</h6>
                        </div>
                        <div class="card-body">
                            {% if transaction.status == 'succeeded' %}
                                <!-- Transazione completata -->
                                <div class="alert alert-success p-2 mb-3">
                                    <small><strong>✅ Pagamento completato con successo!</strong></small>
                                </div>
                                
                                {% if is_buyer %}
                                    <p><small>Il venditore è stato notificato del pagamento.</small></p>
                                {% elif is_seller %}
                                    <p><small>Organizza la consegna con l'acquirente.</small></p>
                                {% endif %}
                                
                            {% elif transaction.status == 'pending' or transaction.status == 'processing' %}
                                <!-- In attesa/elaborazione -->
                                <div class="alert alert-warning p-2 mb-3">
                                    <small><strong>⏳ Pagamento in elaborazione...</strong></small>
                                </div>
                                <p><small>La transazione verrà completata a breve.</small></p>
                                
                            {% elif transaction.status == 'failed' %}
                                <!-- Fallita -->
                                <div class="alert alert-danger p-2 mb-3">
                                    <small><strong>❌ Pagamento fallito</strong></small>
                                </div>
                                {% if is_buyer %}
                                    <p><small>Puoi riprovare o contattare il supporto.</small></p>
                                {% endif %}
                            {% endif %}
                            
                            <!-- Link alle cronologie -->
                            {% if is_buyer %}
                                <a href="{% url 'payments:purchase_history' %}" 
                                   class="btn btn-outline-primary btn-sm btn-block">
                                    📋 I Miei Acquisti
                                </a>
                            {% elif is_seller %}
                                <a href="{% url 'payments:sales_history' %}" 
                                   class="btn btn-outline-success btn-sm btn-block">
                                    📋 Le Mie Vendite
                                </a>
                            {% endif %}
                        </div>
                    </div>
                    
                    <!-- Link Stripe -->
                    {% if transaction.stripe_payment_intent_id and is_seller %}
                    <div class="card">
                        <div class="card-body text-center">
                            <small class="text-muted">
                                ID Stripe: {{ transaction.stripe_payment_intent_id|slice:":20" }}...
                            </small>
                        </div>
                    </div>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Auto-refresh per transazioni in corso -->
{% if transaction.status == 'pending' or transaction.status == 'processing' %}
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Refresh ogni 30 secondi per transazioni in corso
    setTimeout(function() {
        window.location.reload();
    }, 30000);
});
</script>
{% endif %}
{% endblock %}
```


### templates/registration/registration_complete.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n %}

{% block title %}{% trans "Registrazione completata" %}{% endblock %}

{% block body %}
<div class="container" style="max-width:500px; margin-top:30px;">
  <h3>{% trans "Registrazione completata!" %}</h3>
  <p>{% trans "Ora puoi accedere al tuo account con le credenziali scelte." %}</p>
  <a href="{% url 'login' %}" class="btn btn-primary">{% trans "Vai al login" %}</a>
</div>
{% endblock %}
```


### templates/registration/registration_form.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n %}

{% block title %}{% trans "Registrazione" %}{% endblock %}

{% block body %}
<div class="container" style="max-width:500px; margin-top:30px;">
  <h3>{% trans "Crea un nuovo account" %}</h3>

  <form method="post" action="">
    {% csrf_token %}
    {{ form.non_field_errors }}

    <div class="form-group">
      <label for="id_username">{% trans "Username" %}</label>
      {{ form.username }}
      {{ form.username.errors }}
    </div>

    <div class="form-group">
      <label for="id_email">{% trans "Email" %}</label>
      {{ form.email }}
      {{ form.email.errors }}
    </div>

    <div class="form-group">
      <label for="id_password1">{% trans "Password" %}</label>
      {{ form.password1 }}
      {{ form.password1.errors }}
    </div>

    <div class="form-group">
      <label for="id_password2">{% trans "Conferma password" %}</label>
      {{ form.password2 }}
      {{ form.password2.errors }}
    </div>

    <button type="submit" class="btn btn-success btn-block">{% trans "Registrati" %}</button>
  </form>

  <div style="margin-top:15px;">
    <p>{% trans "Hai già un account?" %} <a href="{% url 'login' %}">{% trans "Accedi" %}</a></p>
  </div>
</div>
{% endblock %}
```


### templates/trade/detail.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n widget_tweaks %}

{% block title %}Dettagli Scambio #{{ trade.pk }}{% endblock %}

{% block body %}
<div class="container" style="max-width: 900px;">
    <h3>🔄 Scambio #{{ trade.pk }}</h3>
    
    <!-- Status -->
    <div class="row mb-3">
        <div class="col-md-12">
            <div class="alert 
                {% if trade.state == 'sent' %}alert-warning
                {% elif trade.state == 'accepted' %}alert-success
                {% elif trade.state == 'completed' %}alert-info
                {% elif trade.state == 'declined' %}alert-danger
                {% else %}alert-secondary{% endif %}">
                <h4>
                    {% if trade.state == 'sent' %}⏳ In Attesa di Risposta
                    {% elif trade.state == 'accepted' %}✅ Scambio Accettato
                    {% elif trade.state == 'completed' %}🎉 Scambio Completato
                    {% elif trade.state == 'declined' %}❌ Scambio Rifiutato
                    {% elif trade.state == 'cancelled' %}🚫 Scambio Annullato
                    {% endif %}
                </h4>
                <p class="mb-0">Data: {{ trade.created_at|date:"d/m/Y H:i" }}</p>
            </div>
        </div>
    </div>

    <!-- Dettagli Scambio -->
    <div class="row mb-4">
        <!-- Annuncio Offerto -->
        <div class="col-md-6">
            <div class="card">
                <div class="card-header bg-primary text-white">
                    <h5>📤 {{ trade.from_user.username }} Offre</h5>
                </div>
                <div class="card-body">
                    {% if trade.offer_item.image_set.first %}
                        <img src="{{ trade.offer_item.image_set.first.file.url }}" alt="{{ trade.offer_item.title }}" 
                             class="img-fluid mb-3 rounded" style="max-height: 200px; width: 100%; object-fit: cover;">
                    {% endif %}
                    <h6><a href="{{ trade.offer_item.get_absolute_url }}" target="_blank">{{ trade.offer_item.title }}</a></h6>
                    <p><strong>Prezzo:</strong> {{ trade.offer_item.price|floatformat:0 }}€</p>
                    {% if trade.offer_item.description %}
                        <p class="text-muted small">{{ trade.offer_item.description|truncatewords:15 }}</p>
                    {% endif %}
                </div>
            </div>
        </div>

        <!-- Annuncio Richiesto -->
        <div class="col-md-6">
            <div class="card">
                <div class="card-header bg-success text-white">
                    <h5>📥 {{ trade.to_user.username }} Riceve</h5>
                </div>
                <div class="card-body">
                    {% if trade.want_item.image_set.first %}
                        <img src="{{ trade.want_item.image_set.first.file.url }}" alt="{{ trade.want_item.title }}" 
                             class="img-fluid mb-3 rounded" style="max-height: 200px; width: 100%; object-fit: cover;">
                    {% endif %}
                    <h6><a href="{{ trade.want_item.get_absolute_url }}" target="_blank">{{ trade.want_item.title }}</a></h6>
                    <p><strong>Prezzo:</strong> {{ trade.want_item.price|floatformat:0 }}€</p>
                    {% if trade.want_item.description %}
                        <p class="text-muted small">{{ trade.want_item.description|truncatewords:15 }}</p>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>

    <!-- Messaggio Iniziale -->
    {% if trade.message %}
    <div class="row mb-4">
        <div class="col-md-12">
            <div class="card">
                <div class="card-header">
                    <h5>💬 Messaggio di {{ trade.from_user.username }}</h5>
                </div>
                <div class="card-body">
                    <p>{{ trade.message|linebreaks }}</p>
                </div>
            </div>
        </div>
    </div>
    {% endif %}

    <!-- Azioni Scambio Pendente -->
    {% if trade.state == 'sent' %}
        <div class="row mb-4">
            <div class="col-md-12">
                <div class="card">
                    <div class="card-header">
                        <h5>⚡ Azioni Disponibili</h5>
                    </div>
                    <div class="card-body text-center">
                        {% if user == trade.to_user %}
                            <form method="post" action="{% url 'trade:action' trade.pk 'accept' %}" style="display:inline; margin-right: 10px;">
                                {% csrf_token %}
                                <button type="submit" class="btn btn-success btn-lg"
                                        onclick="return confirm('✅ Accettare questo scambio?')">
                                    ✅ Accetta Scambio
                                </button>
                            </form>
                            <form method="post" action="{% url 'trade:action' trade.pk 'decline' %}" style="display:inline;">
                                {% csrf_token %}
                                <button type="submit" class="btn btn-danger btn-lg"
                                        onclick="return confirm('❌ Sei sicuro di rifiutare questo scambio?')">
                                    ❌ Rifiuta
                                </button>
                            </form>
                        {% elif user == trade.from_user %}
                            <p class="text-muted">In attesa di risposta da {{ trade.to_user.username }}...</p>
                            <form method="post" action="{% url 'trade:action' trade.pk 'cancel' %}" style="display:inline;">
                                {% csrf_token %}
                                <button type="submit" class="btn btn-warning"
                                        onclick="return confirm('🚫 Annullare la proposta?')">
                                    🚫 Annulla Proposta
                                </button>
                            </form>
                        {% endif %}
                    </div>
                </div>
            </div>
        </div>

    <!-- SEZIONE SCAMBIO ACCETTATO - COMUNICAZIONE INTERNA -->
    {% elif trade.state == 'accepted' %}
        <div class="row mb-4">
            <div class="col-md-12">
                <div class="alert alert-success">
                    <h4>✅ Scambio Accettato!</h4>
                    <p>Organizzate insieme il vostro scambio utilizzando la messaggistica qui sotto oppure i contatti diretti.</p>
                </div>
            </div>
        </div>

        <!-- Informazioni di Contatto -->
        <div class="row mb-4">
            <div class="col-md-6">
                <div class="card border-primary">
                    <div class="card-header bg-primary text-white">
                        <h5>👤 {{ trade.from_user.username }} (Offerente)</h5>
                    </div>
                    <div class="card-body">
                        {% if trade.from_user.trade_profile_extended %}
                            {% if trade.from_user.trade_profile_extended.phone_number and trade.from_user.trade_profile_extended.show_phone_in_trades %}
                                <p><strong>📞 Telefono:</strong> 
                                    <a href="tel:{{ trade.from_user.trade_profile_extended.phone_number }}">
                                        {{ trade.from_user.trade_profile_extended.phone_number }}
                                    </a>
                                </p>
                            {% else %}
                                <p class="text-muted">📞 Telefono: 
                                    {% if not trade.from_user.trade_profile_extended.phone_number %}
                                        Non impostato
                                    {% else %}
                                        Nascosto dall'utente
                                    {% endif %}
                                </p>
                            {% endif %}
                            
                            {% if trade.from_user.trade_profile_extended.location %}
                                <p><strong>📍 Zona:</strong> {{ trade.from_user.trade_profile_extended.location }}</p>
                            {% else %}
                                <p class="text-muted">📍 Zona: Non impostata</p>
                            {% endif %}
                        {% else %}
                            <p class="text-muted">❌ Profilo non trovato</p>
                        {% endif %}
                        
                        {% if trade.from_user.email %}
                            <p><strong>✉️ Email:</strong> {{ trade.from_user.email }}</p>
                        {% endif %}
                    </div>
                </div>
            </div>
            
            <div class="col-md-6">
                <div class="card border-success">
                    <div class="card-header bg-success text-white">
                        <h5>👤 {{ trade.to_user.username }} (Ricevente)</h5>
                    </div>
                    <div class="card-body">
                        {% if trade.to_user.trade_profile_extended %}
                            {% if trade.to_user.trade_profile_extended.phone_number and trade.to_user.trade_profile_extended.show_phone_in_trades %}
                                <p><strong>📞 Telefono:</strong> 
                                    <a href="tel:{{ trade.to_user.trade_profile_extended.phone_number }}">
                                        {{ trade.to_user.trade_profile_extended.phone_number }}
                                    </a>
                                </p>
                            {% else %}
                                <p class="text-muted">📞 Telefono: 
                                    {% if not trade.to_user.trade_profile_extended.phone_number %}
                                        Non impostato
                                    {% else %}
                                        Nascosto dall'utente
                                    {% endif %}
                                </p>
                            {% endif %}
                            
                            {% if trade.to_user.trade_profile_extended.location %}
                                <p><strong>📍 Zona:</strong> {{ trade.to_user.trade_profile_extended.location }}</p>
                            {% else %}
                                <p class="text-muted">📍 Zona: Non impostata</p>
                            {% endif %}
                        {% else %}
                            <p class="text-muted">❌ Profilo non trovato</p>
                        {% endif %}
                        
                        {% if trade.to_user.email %}
                            <p><strong>✉️ Email:</strong> {{ trade.to_user.email }}</p>
                        {% endif %}
                    </div>
                </div>
            </div>
        </div>

        <!-- Messaggistica Interna con Supporto Immagini -->
        <div class="row mb-4">
            <div class="col-md-12">
                <div class="card">
                    <div class="card-header bg-info text-white">
                        <h5>💬 Messaggistica Interna</h5>
                    </div>
                    <div class="card-body">
                        <!-- Cronologia Messaggi con Immagini -->
                        {% if trade_messages %}
                            <div class="messages-history mb-3" style="max-height: 400px; overflow-y: auto; border: 1px solid #dee2e6; border-radius: 5px; padding: 15px; background-color: #f8f9fa;">
                                {% for msg in trade_messages %}
                                    <div class="message mb-3 {% if msg.sender == user %}text-right{% endif %}">
                                        <div class="message-bubble {% if msg.sender == user %}alert-primary{% else %}alert-light{% endif %} alert py-2 px-3" 
                                             style="display: inline-block; max-width: 80%; text-align: left;">
                                            
                                            <!-- Header del messaggio -->
                                            <small class="text-muted">
                                                <strong>{{ msg.sender.username }}</strong> - {{ msg.created_at|date:"d/m/Y H:i" }}
                                            </small>
                                            
                                            <!-- Contenuto testuale -->
                                            {% if msg.message %}
                                                <div class="mt-1">{{ msg.message|linebreaks }}</div>
                                            {% endif %}
                                            
                                            <!-- Immagine allegata -->
                                            {% if msg.image %}
                                                <div class="mt-2">
                                                    <div class="image-container" style="position: relative;">
                                                        <!-- Thumbnail cliccabile -->
                                                        <img src="{% if msg.get_image_thumbnail_url %}{{ msg.get_image_thumbnail_url }}{% else %}{{ msg.image.url }}{% endif %}" 
                                                             alt="Immagine allegata" 
                                                             class="img-fluid rounded shadow-sm message-image"
                                                             style="max-width: 100%; cursor: pointer; border: 2px solid #dee2e6;"
                                                             onclick="openImageModal('{{ msg.image.url }}', '{{ msg.sender.username }}', '{{ msg.created_at|date:"d/m/Y H:i" }}')">
                                                        
                                                        <!-- Overlay con info -->
                                                        <div class="image-overlay" style="position: absolute; bottom: 5px; right: 5px; background: rgba(0,0,0,0.7); color: white; padding: 2px 6px; border-radius: 3px; font-size: 0.7em;">
                                                            📷 Clicca per ingrandire
                                                        </div>
                                                        
                                                        <!-- Dimensione file -->
                                                        {% if msg.get_file_size_display %}
                                                            <div class="file-size text-muted" style="font-size: 0.8em; margin-top: 5px;">
                                                                📁 {{ msg.get_file_size_display }}
                                                            </div>
                                                        {% endif %}
                                                    </div>
                                                </div>
                                            {% endif %}
                                        </div>
                                    </div>
                                {% endfor %}
                            </div>
                        {% else %}
                            <p class="text-muted text-center">Nessun messaggio ancora. Inizia la conversazione qui sotto!</p>
                        {% endif %}

                        <!-- Form Nuovo Messaggio con Supporto Immagini -->
                        {% if message_form %}
                            <form method="post" action="{% url 'trade:send_message' trade.pk %}" enctype="multipart/form-data">
                                {% csrf_token %}
                                
                                <div class="form-group">
                                    <label for="id_message">💬 Scrivi un messaggio:</label>
                                    {{ message_form.message|add_class:"form-control" }}
                                    {% if message_form.message.errors %}
                                        <div class="text-danger">{{ message_form.message.errors }}</div>
                                    {% endif %}
                                </div>
                                
                                <div class="form-group">
                                    <label for="id_image">📷 Allega Immagine (opzionale):</label>
                                    {{ message_form.image|add_class:"form-control-file" }}
                                    {% if message_form.image.errors %}
                                        <div class="text-danger">{{ message_form.image.errors }}</div>
                                    {% endif %}
                                    <small class="form-text text-muted">Formati supportati: JPG, PNG, GIF (max 5MB)</small>

<<TRUNCATED FILE: limited to 300 lines>>
```


### templates/trade/inbox.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n %}

{% block title %}Scambi Ricevuti{% endblock %}

{% block body %}
<div class="container">
    <h3>📥 Scambi Ricevuti {% if pending_count %}<span class="badge badge-warning">{{ pending_count }}</span>{% endif %}</h3>
    
    <div class="row mb-3">
        <div class="col-md-6">
            <a href="{% url 'trade:inbox' %}" class="btn btn-primary">📥 Ricevuti</a>
            <a href="{% url 'trade:sent' %}" class="btn btn-outline-secondary">📤 Inviati</a>
        </div>
    </div>

    {% if trades %}
        <div class="table-responsive">
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>Da</th>
                        <th>Offre</th>
                        <th>Per</th>
                        <th>Stato</th>
                        <th>Data</th>
                        <th>Azioni</th>
                    </tr>
                </thead>
                <tbody>
                    {% for trade in trades %}
                    <tr>
                        <td>
                            <strong>{{ trade.from_user.username }}</strong>
                        </td>
                        <td>
                            <a href="{{ trade.offer_item.get_absolute_url }}">{{ trade.offer_item.title }}</a>
                        </td>
                        <td>
                            <a href="{{ trade.want_item.get_absolute_url }}">{{ trade.want_item.title }}</a>
                        </td>
                        <td>
                            {% if trade.state == 'sent' %}
                                <span class="badge badge-warning">⏳ {{ trade.get_state_display }}</span>
                            {% elif trade.state == 'accepted' %}
                                <span class="badge badge-success">✅ {{ trade.get_state_display }}</span>
                            {% elif trade.state == 'declined' %}
                                <span class="badge badge-danger">❌ {{ trade.get_state_display }}</span>
                            {% elif trade.state == 'completed' %}
                                <span class="badge badge-info">🎉 {{ trade.get_state_display }}</span>
                            {% else %}
                                <span class="badge badge-secondary">{{ trade.get_state_display }}</span>
                            {% endif %}
                        </td>
                        <td>{{ trade.created_at|date:"d/m/Y" }}</td>
                        <td>
                            {% if trade.state == 'sent' %}
                                <div class="btn-group btn-group-sm">
                                    <form method="post" action="{% url 'trade:action' trade.pk 'accept' %}" style="display:inline;">
                                        {% csrf_token %}
                                        <button type="submit" class="btn btn-success btn-sm"
                                                onclick="return confirm('✅ Accettare questo scambio?')">
                                            ✅ Accetta
                                        </button>
                                    </form>
                                    <form method="post" action="{% url 'trade:action' trade.pk 'decline' %}" style="display:inline;">
                                        {% csrf_token %}
                                        <button type="submit" class="btn btn-danger btn-sm"
                                                onclick="return confirm('❌ Rifiutare questo scambio?')">
                                            ❌ Rifiuta
                                        </button>
                                    </form>
                                </div>
                            {% elif trade.state == 'accepted' %}
                                <form method="post" action="{% url 'trade:action' trade.pk 'complete' %}" style="display:inline;">
                                    {% csrf_token %}
                                    <button type="submit" class="btn btn-primary btn-sm"
                                            onclick="return confirm('🎉 Completare questo scambio?')">
                                        🎉 Completa
                                    </button>
                                </form>
                            {% endif %}
                            
                            {% if trade.message %}
                                <button class="btn btn-info btn-sm" title="{{ trade.message }}" 
                                        data-toggle="tooltip" data-placement="top">💬</button>
                            {% endif %}
                            
                            <a href="{% url 'trade:detail' trade.pk %}" class="btn btn-secondary btn-sm">
                                👁️ Dettagli
                            </a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>

        {% if is_paginated %}
        <div class="text-center">
            <div class="pagination">
                {% if page_obj.has_previous %}
                    <a href="?page={{ page_obj.previous_page_number }}">&laquo; Precedente</a>
                {% endif %}
                
                Pagina {{ page_obj.number }} di {{ page_obj.paginator.num_pages }}
                
                {% if page_obj.has_next %}
                    <a href="?page={{ page_obj.next_page_number }}">Successiva &raquo;</a>
                {% endif %}
            </div>
        </div>
        {% endif %}

    {% else %}
        <div class="alert alert-info">
            <h4>📭 Nessuno Scambio Ricevuto</h4>
            <p>Non hai ancora ricevuto proposte di scambio.</p>
            <a href="{% url 'django_classified:index' %}" class="btn btn-primary">Esplora Annunci</a>
        </div>
    {% endif %}
</div>
{% endblock %}
```


### templates/trade/propose.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n widget_tweaks %}

{% block title %}Proponi Scambio{% endblock %}

{% block body %}
<div class="container" style="max-width: 800px;">
    <h3>🔄 Proponi uno Scambio</h3>
    
    <!-- Annuncio target -->
    <div class="card mb-4">
        <div class="card-header bg-info text-white">
            <h5>📝 Annuncio Richiesto</h5>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-md-3">
                    {% if want_item.image %}
                        <img src="{{ want_item.image.url }}" alt="{{ want_item.title }}" class="img-fluid rounded">
                    {% else %}
                        <div class="bg-light p-3 text-center rounded">Nessuna Immagine</div>
                    {% endif %}
                </div>
                <div class="col-md-9">
                    <h5>{{ want_item.title }}</h5>
                    <p><strong>Proprietario:</strong> {{ want_item.user.username }}</p>
                    <p><strong>Prezzo:</strong> {{ want_item.price }}{{ want_item.currency }}</p>
                    {% if want_item.description %}
                        <p class="text-muted">{{ want_item.description|truncatewords:20 }}</p>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>

    {% if not has_items %}
        <!-- Nessun annuncio disponibile -->
        <div class="alert alert-warning">
            <h4>⚠️ Nessun Annuncio Disponibile</h4>
            <p>Non hai annunci attivi da offrire per questo scambio.</p>
            <a href="{% url 'django_classified:item-new' %}" class="btn btn-success">✨ Pubblica un Annuncio</a>
            <a href="{{ want_item.get_absolute_url }}" class="btn btn-secondary">↩️ Torna all'Annuncio</a>
        </div>
    {% else %}
        <!-- Form proposta -->
        <form method="post">
            {% csrf_token %}
            
            <div class="card mb-4">
                <div class="card-header">
                    <h5>🎁 I Tuoi Annunci</h5>
                </div>
                <div class="card-body">
                    <div class="form-group">
                        <label for="{{ form.offer_item.id_for_label }}">Seleziona cosa vuoi offrire:</label>
                        {{ form.offer_item|add_class:"form-control form-control-lg" }}
                        {% if form.offer_item.errors %}
                            <div class="text-danger">{{ form.offer_item.errors }}</div>
                        {% endif %}
                    </div>
                </div>
            </div>

            <div class="card mb-4">
                <div class="card-header">
                    <h5>💬 Messaggio</h5>
                </div>
                <div class="card-body">
                    <div class="form-group">
                        <label for="{{ form.message.id_for_label }}">Messaggio per {{ want_item.user.username }} (opzionale):</label>
                        {{ form.message|add_class:"form-control" }}
                        {% if form.message.errors %}
                            <div class="text-danger">{{ form.message.errors }}</div>
                        {% endif %}
                    </div>
                </div>
            </div>

            <!-- Bottoni -->
            <div class="text-center">
                <button type="submit" class="btn btn-success btn-lg">
                    📤 Invia Proposta di Scambio
                </button>
                <a href="{{ want_item.get_absolute_url }}" class="btn btn-secondary btn-lg">
                    ❌ Annulla
                </a>
            </div>
        </form>
    {% endif %}
</div>
{% endblock %}
```


### templates/trade/sent.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n %}

{% block title %}Scambi Inviati{% endblock %}

{% block body %}
<div class="container">
    <h3>📤 Scambi Inviati</h3>
    
    <div class="row mb-3">
        <div class="col-md-6">
            <a href="{% url 'trade:inbox' %}" class="btn btn-outline-secondary">📥 Ricevuti</a>
            <a href="{% url 'trade:sent' %}" class="btn btn-primary">📤 Inviati</a>
        </div>
    </div>

    {% if trades %}
        <div class="table-responsive">
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>A</th>
                        <th>Ho Offerto</th>
                        <th>Per</th>
                        <th>Stato</th>
                        <th>Data</th>
                        <th>Azioni</th>
                    </tr>
                </thead>
                <tbody>
                    {% for trade in trades %}
                    <tr>
                        <td><strong>{{ trade.to_user.username }}</strong></td>
                        <td><a href="{{ trade.offer_item.get_absolute_url }}">{{ trade.offer_item.title }}</a></td>
                        <td><a href="{{ trade.want_item.get_absolute_url }}">{{ trade.want_item.title }}</a></td>
                        <td>
                            {% if trade.state == 'sent' %}
                                <span class="badge badge-warning">⏳ In Attesa</span>
                            {% elif trade.state == 'accepted' %}
                                <span class="badge badge-success">✅ Accettata</span>
                            {% elif trade.state == 'declined' %}
                                <span class="badge badge-danger">❌ Rifiutata</span>
                            {% elif trade.state == 'completed' %}
                                <span class="badge badge-info">🎉 Completata</span>
                            {% elif trade.state == 'cancelled' %}
                                <span class="badge badge-secondary">🚫 Annullata</span>
                            {% endif %}
                        </td>
                        <td>{{ trade.created_at|date:"d/m/Y" }}</td>
                        <td>
                            {% if trade.state == 'sent' or trade.state == 'accepted' %}
                                <form method="post" action="{% url 'trade:action' trade.pk 'cancel' %}" style="display:inline;">
                                    {% csrf_token %}
                                    <button type="submit" class="btn btn-warning btn-sm"
                                            onclick="return confirm('🚫 Annullare questo scambio?')">
                                        🚫 Annulla
                                    </button>
                                </form>
                            {% endif %}
                            
                            {% if trade.state == 'accepted' %}
                                <form method="post" action="{% url 'trade:action' trade.pk 'complete' %}" style="display:inline;">
                                    {% csrf_token %}
                                    <button type="submit" class="btn btn-primary btn-sm"
                                            onclick="return confirm('🎉 Completare questo scambio?')">
                                        🎉 Completa
                                    </button>
                                </form>
                            {% endif %}
                            
                            <a href="{% url 'trade:detail' trade.pk %}" class="btn btn-secondary btn-sm">
                                👁️ Dettagli
                            </a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    {% else %}
        <div class="alert alert-info">
            <h4>📭 Nessuna Proposta Inviata</h4>
            <p>Non hai ancora inviato proposte di scambio.</p>
            <a href="{% url 'django_classified:index' %}" class="btn btn-primary">Cerca Annunci da Scambiare</a>
        </div>
    {% endif %}
</div>
{% endblock %}
```


### templates/trade/user_profile.html

```html
{% extends "django_classified/_base.html" %}
{% load i18n widget_tweaks %}

{% block title %}Il Mio Profilo{% endblock %}

{% block body %}
<div class="container" style="max-width: 700px;">
    <h3>👤 Il Mio Profilo</h3>
    
    <div class="card">
        <div class="card-header bg-primary text-white">
            <h5>📝 Informazioni di Contatto</h5>
        </div>
        <div class="card-body">
            <div class="alert alert-info">
                <h6>ℹ️ Perché compilare queste informazioni?</h6>
                <p class="mb-0">Queste informazioni saranno visibili <strong>solo agli utenti con cui hai scambi accettati</strong> per facilitare l'organizzazione dello scambio fisico.</p>
            </div>
            
            <form method="post">
                {% csrf_token %}
                
                <h6>📞 Contatto Telefonico</h6>
                <div class="form-group">
                    <label for="{{ form.phone_number.id_for_label }}">Numero di Telefono:</label>
                    {{ form.phone_number|add_class:"form-control" }}
                    {% if form.phone_number.errors %}
                        <div class="text-danger">{{ form.phone_number.errors }}</div>
                    {% endif %}
                    <small class="form-text text-muted">Formato suggerito: +39 123 456 7890</small>
                </div>

                <div class="form-group form-check">
                    {{ form.show_phone_in_trades|add_class:"form-check-input" }}
                    <label class="form-check-label" for="{{ form.show_phone_in_trades.id_for_label }}">
                        Mostra il mio numero di telefono negli scambi accettati
                    </label>
                    {% if form.show_phone_in_trades.errors %}
                        <div class="text-danger">{{ form.show_phone_in_trades.errors }}</div>
                    {% endif %}
                </div>

                <hr>

                <h6>📍 Localizzazione</h6>
                <div class="form-group">
                    <label for="{{ form.location.id_for_label }}">Città/Zona:</label>
                    {{ form.location|add_class:"form-control" }}
                    {% if form.location.errors %}
                        <div class="text-danger">{{ form.location.errors }}</div>
                    {% endif %}
                    <small class="form-text text-muted">Es. Milano, Roma, Napoli, etc. Aiuta gli altri utenti a sapere se siete nella stessa zona</small>
                </div>

                <hr>

                <div class="text-center">
                    <button type="submit" class="btn btn-primary btn-lg">💾 Salva Profilo</button>
                    <a href="{% url 'django_classified:index' %}" class="btn btn-secondary">❌ Annulla</a>
                </div>
            </form>
        </div>
    </div>

    <!-- Statistiche Scambi -->
    <div class="card mt-4">
        <div class="card-header bg-success text-white">
            <h5>📊 Le Mie Statistiche</h5>
        </div>
        <div class="card-body">
            {% if user.trade_profile %}
                <div class="row">
                    <div class="col-md-4 text-center">
                        <h4 class="text-primary">{{ user.trade_profile.total_trades_completed }}</h4>
                        <p class="text-muted">Scambi Completati</p>
                    </div>
                    <div class="col-md-4 text-center">
                        <h4 class="text-warning">{{ user.trade_profile.average_rating|floatformat:1 }}/5 ⭐</h4>
                        <p class="text-muted">Rating Medio</p>
                    </div>
                    <div class="col-md-4 text-center">
                        <h4 class="text-info">{{ user.trade_profile.total_feedbacks_received }}</h4>
                        <p class="text-muted">Valutazioni Ricevute</p>
                    </div>
                </div>
            {% else %}
                <p class="text-muted text-center">Completa il tuo primo scambio per vedere le statistiche!</p>
            {% endif %}
        </div>
    </div>

    <!-- Informazioni Attuali -->
    {% if profile.phone_number or profile.location %}
    <div class="card mt-4">
        <div class="card-header bg-info text-white">
            <h5>👁️ Anteprima delle Tue Informazioni</h5>
        </div>
        <div class="card-body">
            <p class="text-muted">Ecco come vedranno le tue informazioni gli altri utenti negli scambi accettati:</p>
            
            <div class="card border-primary">
                <div class="card-header bg-primary text-white">
                    <h6>👤 {{ user.username }}</h6>
                </div>
                <div class="card-body">
                    {% if profile.phone_number and profile.show_phone_in_trades %}
                        <p><strong>📞 Telefono:</strong> {{ profile.phone_number }}</p>
                    {% else %}
                        <p class="text-muted">📞 Telefono: Non disponibile</p>
                    {% endif %}
                    

<<TRUNCATED CONTEXT: limited to 5000 total lines>>