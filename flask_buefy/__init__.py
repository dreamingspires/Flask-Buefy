from flask import Blueprint, current_app
from flask_assets import Environment, Bundle

BUEFY_VERSION = 'latest'
FONTAWESOME_VERSION = '5.2.0'
MATERIALDESIGN_VERSION = '5.3.45'

class Buefy():
    def __init__(self, app=None):
        if app is not None:
            # Initialise flask_assets if not already initialised
            try:
                assets = app.jinja_env.assets_environment
            except AttributeError:
                assets = Environment(app)

            self.init_app(app, assets)

    def init_app(self, app, assets):
        app.config.setdefault('BUEFY_ICON_PACK', 'fas')
        app.config.setdefault('VUE_DEVEL', False)

        blueprint = Blueprint(
            'buefy',
            __name__,
            template_folder='templates',)
            #static_folder='static',
            #static_url_path=app.static_url_path + '/buefy')

        # Add template filters
        # blueprint.add_app_template_filter(render_form)

        app.register_blueprint(blueprint)

        # Add Vue.js bundles
        vue_js = Bundle('https://cdn.jsdelivr.net/npm/vue@2')
        assets.register('vue_js', vue_js)
        vue_devel_js = Bundle('https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js')
        assets.register('vue_devel_js', vue_devel_js)

        # Add Buefy bundles
        buefy_min_css = Bundle('https://unpkg.com/buefy/dist/buefy.min.css')
        assets.register('buefy_min_css', buefy_min_css)
        buefy_min_js = Bundle('https://unpkg.com/buefy/dist/buefy.min.js')
        assets.register('buefy_min_js', buefy_min_js)

        # Add icon pack bundles
        fontawesome_css = Bundle(f'https://use.fontawesome.com/releases/v{FONTAWESOME_VERSION}/css/all.css')
        assets.register('fontawesome_css', fontawesome_css)
        materialdesign_css = Bundle(f'https://cdn.materialdesignicons.com/{MATERIALDESIGN_VERSION}/css/materialdesignicons.min.css')
        assets.register('materialdesign_css', materialdesign_css)

        # Eventual support for flask-nav goes here
