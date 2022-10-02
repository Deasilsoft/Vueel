module.exports = {
    pages: {
        index: {
            entry: "ui/main.js",
            template: "ui/index.html",
        },
    },
    outputDir: "storage/ui",
    css: {
        extract: true,
    },
    devServer: {
        writeToDisk: true,
    }
}
