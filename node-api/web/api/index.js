/*
 * Index file to route to different API
 * modules such as search
 */

const apiRouter = require("express").Router();
const search = require("./search")


// Route handlers
apiRouter.use('/search', search)

module.exports = apiRouter;
