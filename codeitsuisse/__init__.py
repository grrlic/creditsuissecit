from flask import Flask
app = Flask(__name__, template_folder='views')

import codeitsuisse.routes.bored_scribe
import codeitsuisse.routes.bucket_fill
import codeitsuisse.routes.clean_floor
import codeitsuisse.routes.cluster
import codeitsuisse.routes.contact_trace
import codeitsuisse.routes.fruit_basket
import codeitsuisse.routes.intelligent_farming
import codeitsuisse.routes.inventory_management
import codeitsuisse.routes.olympiad_of_babylon
import codeitsuisse.routes.optimized_portfolio
import codeitsuisse.routes.revisit_geometry
import codeitsuisse.routes.salad_spree
import codeitsuisse.routes.secret_message
import codeitsuisse.routes.snakes_ladders_smoke_mirrors
import codeitsuisse.routes.social_distancing
import codeitsuisse.routes.square
import codeitsuisse.routes.supermarket_maze
import codeitsuisse.routes.swap_hedge
import codeitsuisse.routes.yin_yang