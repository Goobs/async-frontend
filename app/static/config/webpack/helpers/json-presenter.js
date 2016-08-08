'use strict';

module.exports = function(data, parsedAssets) {
 var output = {},
     obj = parsedAssets;

  for (var key in obj) {
   var newkey = key.split('/').pop();
   obj[newkey] = obj[key];
   delete obj[key]
 }

 output.publicPath = data.publicPath;

  for (var key in data.assetsByChunkName) if (data.assetsByChunkName.hasOwnProperty(key)) {
    var value = data.assetsByChunkName[key];

    if (typeof(value) === 'string') {
       reformat(value);
       continue;
    }

    value.forEach(reformat);
  }

 function reformat(filename) {
   var newkey = filename.split('/').pop();
   newkey = newkey.split('.');
   newkey.splice(1,1);
   newkey = newkey.join('.');
   obj[newkey] = filename;
 }

 output.assets = obj;

 return output;
};