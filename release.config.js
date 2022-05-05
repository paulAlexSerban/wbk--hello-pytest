module.exports = {
  branches: "main",
  repositoryUrl: "https://github.com/paulAlexSerban/tpl---reverse-proxy-web-server",
  plugins: [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    [
      "@semantic-release/github",
      {
        assets: [
          {path: "build.zip", label: "Build"}
        ]
      }
    ]
  ],
};
