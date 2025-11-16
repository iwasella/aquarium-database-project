var express = require('express');

const item_options_controller = require("../controllers/itemOptionsController");
const menu_controller = require("../controllers/menuController");
const order_controller = require("../controllers/orderController");
const reservation_controller = require("../controllers/reservationController");

var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.redirect('/store/menu');
});

router.get("/menu", menu_controller.menu_get);
router.post("/menu", menu_controller.menu_post);

router.get("/item-options/:id", item_options_controller.item_options_get);
router.get("/item-options/:id", item_options_controller.item_options_post);

router.get("/order", order_controller.order_get);
router.get("/order", order_controller.order_post);

router.get("/reservation", reservation_controller.reservation_get);
router.get("/reservation", reservation_controller.reservation_post);

module.exports = router;
