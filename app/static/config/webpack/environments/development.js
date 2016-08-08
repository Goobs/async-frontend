'use strict';

/**
 * Development config
 * @param  {String} _path Absolute path to application
 * @return {Object}       Object of development settings
 */
var webpack = require('webpack');
module.exports = function(_path) {

  return {
    context: _path,
    debug: true,
    devtool: 'eval'
  }
};
