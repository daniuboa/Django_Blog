import gql from "graph-tag"

export const SITE_INFO = GQL`
  query {
    site {
        name
    }
  }`