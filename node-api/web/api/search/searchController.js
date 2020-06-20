'use strict';
/*
 * search controller GET, POST, and PUT
 * method
 *
 */

const config = require("../../../config/web")
const logger = config.logger

/*
 * Search in summaries of books
 * @param {obj} req The request object
 * @param {obj} res The response
 *
 * @throws error will throw err
 */
exports.searchSummary = async function (req, res, next) {
  try {
    logger.log("debug", "Req body %o", req.body)
  } catch(error) {
    return res.json({
      success: false,
      message: 'Try catch error in summary search',
      data: {}
    })
  }
}
