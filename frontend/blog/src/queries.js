import gql from "graph-tag";

export const SITE_INFO = gql`
  query {
    site {
      name
    }
  }
`;

export const POST_BY_CATEGORY = gql`
  query($category: String!) {
    postsByCategory(category: $category) {
      title
      slug
      content
      isPublished
      isFeatured
      createdAt
    }
  }
`;
