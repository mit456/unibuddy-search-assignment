'use strict';

/*
 * search controller GET, POST, and PUT
 * method
 *
 */

const config = require("../../../config/web")
const logger = config.logger

const {PythonShell} = require("python-shell")
const path = require("path")
const {spawn} = require("child_process")

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
    logger.log("debug", "Queries", req.body.queries)

    // Pre checks in req body data
    if (!req.body || !req.body.queries) {
      return res.json({
        success: false,
        message: "Required params missing",
        data: []
      })
    }

    if (!req.body || !req.body.responseCount) {
      return res.json({
        success: false,
        message: "Required params missing",
        data: []
      })
    }

    const queries = req.body.queries
    const projectBasepath = path.join(__dirname, "../../../../")
    const searchUtilitypath = path.join(projectBasepath, "utilities/search/core.py")
    const searchType = "summary"
    let queriesCommaSeparated  = ""

    if(queries && Object.keys(queries).length === 0) {
      return res.json({
        success: false,
        message: "Not enough queries to search.",
        data: []
      })
    } else {
      // Build search utility queries for cmd
      Object.keys(queries).forEach(function (key) {
        if (queriesCommaSeparated === "") {
          queriesCommaSeparated = queries[key]
        } else {
          queriesCommaSeparated = queriesCommaSeparated + " , " + queries[key]
        }
      })
    }

    // invoke search utility
    let pyShellOpts = {
      mode: 'text',
      args: ['-qs', queriesCommaSeparated, '-k', req.body.responseCount, '-t', searchType]
    }

    PythonShell.run(searchUtilitypath, pyShellOpts, function(error, results) {
      if(error) {
        logger.log("error", "Error in python search process: %o", error)
        return res.json({
          success: false,
          message: "SERVER_ERROR: Please give us one more attempt or contact to help us resolve it faster",
          data: []
        })
      }

      if (!error && results) {
        return res.json({
          success: true,
          message: "Search results to you queries are:",
          data: JSON.parse(results)
        })
      }
    })
  } catch(error) {
    logger.log("error", "try catch error %o", error.stack)
    return res.json({
      success: false,
      message: "Try catch error in summary search",
      data: []
    })
  }
}
