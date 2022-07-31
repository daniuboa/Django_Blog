import gql from "graphql-tag";

export const SITE_INFO = gql`
  query {
    site {
      name
    }
  }
`;

export const ALL_POSTS = gql`
  query {
    allPosts {
      title
      slug
      content
      isPublished
      isFeatured
      createdAt
      category {
        name
        slug
      }
    }
  }
`;

export const POSTS_BY_CATEGORY = gql`
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

export const POSTS_BY_TAG = gql`
  query($tag: String!) {
    postsByTag(tag: $tag) {
      title
      slug
      content
      isPublished
      isFeatured
      createdAt
      category {
        name
        slug
      }
    }
  }
`;

export const POST_BY_SLUG = gql`
  query($slug: String!) {
    postBySlug(slug: $slug) {
      id
      title
      content
      featuredImage
      createdAt
      category {
        name
        slug
      }
      tag {
        name
        slug
      }
      user {
        id
        username
        firstName
        lastName
      }
      numberOfLikes
      likes {
        id
      }
      commentSet {
        id
        content
        createdAt
        isApproved
        user {
          username
          avatar
        }
        numberOfLikes
        likes {
          id
        }
      }
    }
  }
`;

export const ALL_CATEGORIES = gql`
  query {
    allCategories {
      name
      slug
    }
  }
`;

export const ALL_TAGS = gql`
  query {
    allTags {
      name
      slug
    }
  }
`;

export const CURRENT_USER = gql`
  query($username: String!) {
    currentUser(username: $username) {
      id
      username
      firstName
      lastName
      email
      avatar
      bio
      location
      website
      commentSet {
        id
        content
        post {
          id
          title
          slug
        }
        isApproved
      }
    }
  }
`;
