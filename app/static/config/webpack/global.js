'use strict';

// Depends
var path = require('path');
var webpack = require('webpack');
var Manifest = require('manifest-revision-webpack-plugin');
var autoprefixer = require('autoprefixer-core');
var TextPlugin = require('extract-text-webpack-plugin');
var jsonPresent = require('./helpers/json-presenter');

/**
 * Global webpack config
 * @param  {[type]} _path [description]
 * @return {[type]}       [description]
 */
module.exports = function(_path) {
  // define local variables

  var dependencies = Object.keys(require(_path + '/package').dependencies);
  var rootAssetPath = _path + 'assets';
  var manifestPath = path.join(_path, 'manifest.json');
  var childProcess = require('child_process');
  var _version = childProcess.execSync('git describe').toString();

  _version = _version.replace(/[\s\r\n]+$/, '');

  return {
    entry: {
      vendors: dependencies,
      app: _path + '/assets/js/app.js',

    },

    // output system
    output: {
      path: path.join(_path, 'dist', _version),
      filename: path.join('js', '[name].[hash].js'),
      chunkFilename: '[id].[hash].js',
      publicPath: '/assets/' + _version + '/',
      jsonpFunction: 'rr_webpackJsonp'
    },

    // resolves modules
    resolve: {
      extensions: ['', '.js', '.less'],
      modulesDirectories: ['node_modules'],
      alias: {
        _stylesheets: path.join(_path, 'assets', 'css'),
        _js: path.join(_path, 'assets', 'js'),
        _images: path.join(_path, 'assets', 'img'),
        _fonts: path.join(_path, 'assets', 'fonts')
      }
    },
    module: {
      loaders: [
        {test: /\.json$/, loader: 'json'},
        {test: /\.css$/, loader: TextPlugin.extract('style', 'css')},
        {test: /\.(ttf|eot|woff|woff2|png|ico|jpg|jpeg|gif|svg|pdf|swf|webm|mp4)$/i, loaders: ['file?context=' + rootAssetPath + '&name=[ext]/[name].[hash].[ext]']},
        {test: /\.less$/, loader: TextPlugin.extract('style', 'css!postcss!less')}
      ]
    },

    // post css
    postcss: [autoprefixer({browsers: ['last 3 versions']})],

    // load plugins
    plugins: [
      new webpack.optimize.CommonsChunkPlugin({
        name: 'vendors',
        filename: 'js/vendors.[hash].js'
      }),
      new webpack.ProvidePlugin({
        $: 'jquery',
        jQuery: 'jquery',
        Backbone: 'backbone',
        'window.jQuery': 'jquery',
        _: 'underscore'
      }),
      new TextPlugin('css/[name].[hash].css'),
      new Manifest(manifestPath, {
        rootAssetPath: './assets',
        ignorePaths: ['.DS_Store'],
        format: jsonPresent
      })
    ]
  };
};
