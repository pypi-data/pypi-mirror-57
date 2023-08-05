const path = require('path');
const webpack = require('webpack');

/*
 * Webpack Plugins
 */
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
const ManifestPlugin = require('webpack-manifest-plugin');
const IgnoreEmitPlugin = require('ignore-emit-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

// take debug mode from the environment
const debug = (process.env.NODE_ENV !== 'production');
const hashType = debug ? '[hash]': '[contentHash]'
const rootAssetPath = path.join(__dirname, 'assets');
const publicHost = debug ? 'http://0.0.0.0:2992' : '';

module.exports = {
  // configuration
  context: __dirname,
  entry: {
    main_js: path.join(__dirname, 'assets', 'js', 'main.js'),
    main_css: [
      path.join(__dirname, 'assets', 'css', 'main.css'),
    ],
  },
  output: {
    path: path.join(__dirname, 'app', 'static'),
    publicPath: `${publicHost}/static/`,
    filename: "js/[name]." + hashType + ".js",
    chunkFilename: "js/[name]." + hashType + ".chunk.js"
  },
  optimization: {
  minimizer: [
   new UglifyJsPlugin({
        cache: true,
        parallel: true,
        sourceMap: true,
        uglifyOptions: {
          output: {
            comments: false
          }
        }
    }),
    new OptimizeCssAssetsPlugin({
      assetNameRegExp: /\.css$/g,
      cssProcessor: require('cssnano'),
      cssProcessorPluginOptions: {
        preset: ['default', { discardComments: { removeAll: true } }],
      },
      canPrint: true
    }),
  ],
},
  resolve: {
    extensions: ['.js', '.css'],
  },
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader,
            options: {
              hmr: debug,
            },
          },
          'css-loader',
          {
            loader: 'postcss-loader'
          }
        ],
      },
      { test: /\.html$/, loader: 'raw-loader' },
      { test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: 'url-loader', options: { limit: 10000, mimetype: 'application/font-woff' } },
      { test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader', query: { presets: ['@babel/preset-env'], cacheDirectory: true } },
      {
        test: /\.(ttf|eot|svg|png|jpe?g|gif|ico)(\?.*)?$/i,
        loader: `file-loader?context=${rootAssetPath}&name=[path][name].${hashType}.[ext]`
      },
    ],
  },
  plugins: [
    new IgnoreEmitPlugin(/(?<=main_css\s*).*?(?=\s*js)/gs),
    new MiniCssExtractPlugin({ filename: 'css/[name].' + hashType + '.css', }),
//    new webpack.ProvidePlugin({ $: 'jquery', jQuery: 'jquery' }),

    new ManifestPlugin(
    {
        map: (file) => {
        // Remove hash in manifest key
        file.name = file.name.replace(/(\.[a-f0-9]{32})(\..*)$/, '$2');
        return file;
        },
        writeToFileEmit: true,
    }),
  ].concat(debug ? [] : [
    // production webpack plugins go here
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify('production'),
      } }),

    new CleanWebpackPlugin(),
  ]),
};
