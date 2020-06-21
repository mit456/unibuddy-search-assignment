"use strict";

/*
 * Router for search
 */

const searchRouter = require("express").Router();

const {
  searchSummary
} = require("./searchController.js")

// API router of /api/search
searchRouter.get("/", searchSummary)

module.exports = searchRouter;
