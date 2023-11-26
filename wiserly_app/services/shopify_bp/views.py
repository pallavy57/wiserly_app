import shopify
from flask import (
    Blueprint, render_template, current_app, request, redirect, session,
    url_for)

from services import const

from .models import WiserlyShops
from .decorators import shopify_auth_required
from services.extensions import db
shopify_bp = Blueprint('shopify_bp', __name__,
                       url_prefix='/shopify',
                       static_folder='templates/static',
                       template_folder='templates')


@shopify_bp.route('/')
# @shopify_auth_required
def index():
    """ Render the index page of our application.
    """
    return render_template('index.html')


@shopify_bp.route('/install')
def install():
    """ Redirect user to permission authorization page.
    """

    shop_url = request.args.get("shop")
    shop_url = request.args.get("shop")
    if not shop_url:
        return render_template("400.html", message="No shop in query params"), 400
    shopify.Session.setup(
        api_key=current_app.config['SHOPIFY_API_KEY'],
        secret=current_app.config['SHOPIFY_SHARED_SECRET'])

    session = shopify.Session(
        shop_url, current_app.config['SHOPIFY_API_VERSION'])

    permission_url = session.create_permission_url(
        const.SHOPIFY_OAUTH_SCOPES, url_for("shopify_bp.finalize",
                                            _external=True,
                                            _scheme='https'))

    return render_template(
        'install.html', permission_url=permission_url)


@shopify_bp.route('/finalize')
def finalize():
    """ Generate shop token and store the shop information.

    """

    shop_url = request.args.get("shop")
    shopify.Session.setup(
        api_key=current_app.config['SHOPIFY_API_KEY'],
        secret=current_app.config['SHOPIFY_SHARED_SECRET'])
    shopify_session = shopify.Session(
        shop_url, current_app.config['SHOPIFY_API_VERSION'])

    token = shopify_session.request_token(request.args)

    shop = WiserlyShops(shop=shop_url, token=token)
    db.session.add(shop)
    db.session.commit()

    session['shopify_url'] = shop_url
    session['shopify_token'] = token
    session['shopify_id'] = shop.id

    return redirect(url_for('shopify_bp.index'))
