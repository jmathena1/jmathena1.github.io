import { defineConfig } from "tinacms";

// Your hosting provider likely exposes this as an environment variable
const branch =
  process.env.GITHUB_BRANCH ||
  process.env.VERCEL_GIT_COMMIT_REF ||
  process.env.HEAD ||
  "main";

export const postSchema = [
    {
        type: "string",
        name: "author",
        label: "author",
        required: true,
    },
    {
        type: "string",
        name: "date",
        label: "date",
        required: true,
    },
    {
        type: "string",
        name: "title",
        label: "title",
        required: true,
        isTitle: true,
    },
    { 
        type: "rich-text",
        name: "body",
        label: "body",
        required: true,
        isBody: true,
    },
];

export default defineConfig({
  branch,

  // Get this from tina.io
  clientId: process.env.TINA_PUBLIC_CLIENT_ID,
  // Get this from tina.io
  token: process.env.TINA_TOKEN,

  build: {
    outputFolder: "admin",
    publicFolder: "public",
  },
  media: {
    tina: {
      mediaRoot: "photos",
      publicFolder: "public",
    },
  },
  schema: {
    collections: [
      {
          name: "the_strays_blog_posts",
          label: "The Strays Blog Posts",
          path: "content/the-strays/posts",
          fields: postSchema,
      },
      {
          name: "droppin_dimes_poems",
          label: "Droppin Dimes Poems",
          path: "content/droppin-dimes/posts",
          fields: postSchema,
      },
      {
          name: "wiki_pages",
          label: "Wiki Pages",
          path: "content/wiki-pages",
          fields: [
              {
                  type: "string",
                  name: "title",
                  label: "title",
                  required: true,
                  isTitle: true,
              },
              {
                  type: "string",
                  name: "wikiType",
                  label: "wikiType",
                  required: false,
              },
              {
                  type: "rich-text",
                  name: "body",
                  label: "body",
                  required: true,
                  isBody: true,
              },
          ],
      },
    ],
  },
});
