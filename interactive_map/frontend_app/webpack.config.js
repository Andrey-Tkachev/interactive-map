const path = require("path");
module.exports = {
  entry: ["./src/index.jsx"],
  output: {
    path: path.resolve(__dirname, "./static/js/"),
    filename: "bundle.js"
  },
  mode: "development",
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          query: {
            presets: ["react"],
            plugins: ["transform-object-rest-spread", "transform-class-properties"]
          }
        },
      }
    ]
  }
};
