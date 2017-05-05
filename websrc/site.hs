--------------------------------------------------------------------------------
{-# LANGUAGE OverloadedStrings #-}
import           Data.Monoid (mappend)
import           Hakyll
import	qualified Data.Set as S
import			 Text.Pandoc.Options
import			 Skylighting.Styles (pygments, zenburn)

--------------------------------------------------------------------------------
main :: IO ()
main = hakyll $ do

    match "images/*" $ do
        route   idRoute
        compile copyFileCompiler

    match "css/*" $ do
        route   idRoute
        compile compressCssCompiler

    match "Codes/*" $ do
        route $ setExtension "html"
        compile $ pandocMathCompiler
            >>= loadAndApplyTemplate "templates/post.html"    postCtx
            >>= loadAndApplyTemplate "templates/default.html" postCtx
            >>= relativizeUrls

    match "Slides/*" $ do
        route $ setExtension "html"
        compile $ pandocMathCompiler
            >>= loadAndApplyTemplate "templates/post.html"    postCtx
            >>= loadAndApplyTemplate "templates/default.html" postCtx
            >>= relativizeUrls

    match "resources.md" $ do
        route   $ setExtension "html"
        compile $ pandocMathCompiler
            >>= loadAndApplyTemplate "templates/default.html" defaultContext
            >>= relativizeUrls

    match "index.md" $ do
        route $ setExtension "html"
        compile $ do 
			posts <- recentFirst =<< loadAll "Misc/*"
			let indexCtx =
				listField "posts" postCtx (return posts) `mappend`
				defaultContext
			pandocMathCompiler >>= applyAsTemplate indexCtx
				>>= loadAndApplyTemplate "templates/files.html" indexCtx
				>>= loadAndApplyTemplate "templates/default.html" indexCtx
				>>= relativizeUrls

    match "codes.md" $ do
        route $ setExtension "html"
        compile $ do 
			posts <- recentFirst =<< loadAll "Codes/*"
			let indexCtx =
				listField "posts" postCtx (return posts) `mappend`
				defaultContext
			pandocMathCompiler >>= applyAsTemplate indexCtx
				>>= loadAndApplyTemplate "templates/files.html" indexCtx
				>>= loadAndApplyTemplate "templates/default.html" indexCtx
				>>= relativizeUrls

    match "slides.md" $ do
        route $ setExtension "html"
        compile $ do 
			posts <- recentFirst =<< loadAll "Slides/*"
			let indexCtx =
				listField "posts" postCtx (return posts) `mappend`
				defaultContext
			pandocMathCompiler >>= applyAsTemplate indexCtx
				>>= loadAndApplyTemplate "templates/files.html" indexCtx
				>>= loadAndApplyTemplate "templates/default.html" indexCtx
				>>= relativizeUrls

    match "templates/*" $ compile templateBodyCompiler


--------------------------------------------------------------------------------
postCtx :: Context String
postCtx =
    dateField "date" "%B %e, %Y" `mappend`
    defaultContext

pandocMathCompiler :: Compiler (Item String)
pandocMathCompiler =
    let mathExtensions = [Ext_tex_math_dollars, Ext_tex_math_double_backslash,
                          Ext_latex_macros]
        defaultExtensions = writerExtensions defaultHakyllWriterOptions
        newExtensions = foldr S.insert defaultExtensions mathExtensions
        writerOptions = defaultHakyllWriterOptions {
                          writerExtensions = newExtensions,
						  writerHighlight = True,
						  writerHighlightStyle = zenburn,
                          writerHTMLMathMethod = MathJax ""
                        }
    in pandocCompilerWith defaultHakyllReaderOptions writerOptions


