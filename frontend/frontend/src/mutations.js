import gql from "graphql-tag"

export const USER_SIGNUP = gql`
    mutation ($username: String!, $email: String!, $password: String!) {
        createUser(username: $username, email: $email, password: $password) {
            user {
                id
                username
            }
        }
    }`