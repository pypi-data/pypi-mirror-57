import json

from markdown import markdown

SCRIPT = """<script>
    var loc = String(window.location).replace(/#.*$/, '').replace(/\/$/, '');
    var elements = document.getElementsByTagName('a');
    for (var i = 0; i < elements.length; i++) {
        var a = elements[i];
        if (a.href.indexOf('id://') === 0) {
            var data = {kind: 'addon', url: loc + '/' + a.href.substring(5)};
            a.href = 'https://wtchd.cm/#' + btoa(JSON.stringify(data));
            a.target = '_blank';
        }
    }
</script>
"""


def selectT(s):
    return s


def render_addon(addon):
    return f"""[{selectT(addon['name'])}](id://{addon.id if addon.addon_has_repository else ''})

- Type: `{addon.type}`
- ID: `{addon.id}`
- Version: `{addon['version']}`
"""


def render_body(addon):
    yield '# ' + render_addon(addon)
    if addon['type'] == 'repository':
        for a in addon.addons:
            if a is not addon:
                yield '## ' + render_addon(a)


def render(addon):
    body = markdown('\n\n'.join(render_body(addon)))
    return f"""<!DOCTYPE html>
<html lang = "en">
<head>
  <title> {selectT(addon['name'])} </title>
</head>
<body>
  {body}
  {SCRIPT}
</ body>
</ html>
"""
