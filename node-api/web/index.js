"use strict"

/* /web/index.js
 * description:: Index file to route to api
 */

module.exports = function(app) {
  app.use("/api", require("./api"));
}
