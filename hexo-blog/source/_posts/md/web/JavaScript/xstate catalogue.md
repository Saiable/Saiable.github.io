---
title: 'xstate catalogue'
date: 2023-04-08 09:03:02
cover: false
tags:
- xstate
categories: xstate
typora-root-url: xstate catalogue
---

> https://swimlanes.io/
>
> [XState Catalogue (xstate-catalogue.com)](https://xstate-catalogue.com/#Catalogue)
>
> [XState Visualizer (stately.ai)](https://stately.ai/viz)

# Data Fetching

## Simple Data Fetch



# Global State

## Authentication



```js
import { assign, createMachine, Sender } from 'xstate';

export type AuthenticationMachineContext = {
  userDetails?: UserDetails;
};

interface UserDetails {
  username: string;
}

export type AuthenticationMachineEvent =
  | {
      type: 'REPORT_IS_LOGGED_IN';
      userDetails: UserDetails;
    }
  | {
      type: 'REPORT_IS_LOGGED_OUT';
    }
  | {
      type: 'LOG_OUT';
    }
  | {
      type: 'LOG_IN';
      userDetails: UserDetails;
    };

const authenticationMachine = createMachine<
  AuthenticationMachineContext,
  AuthenticationMachineEvent
>(
  {
    id: 'authentication',
    initial: 'checkingIfLoggedIn',
    states: {
      checkingIfLoggedIn: {
        invoke: {
          src: 'checkIfLoggedIn',
          onError: {
            target: 'loggedOut',
          },
        },
        on: {
          REPORT_IS_LOGGED_IN: {
            target: 'loggedIn',
            actions: 'assignUserDetailsToContext',
          },
          REPORT_IS_LOGGED_OUT: 'loggedOut',
        },
      },
      loggedIn: {
        on: {
          LOG_OUT: {
            target: 'loggedOut',
          },
        },
      },
      loggedOut: {
        entry: ['navigateToAuthPage', 'clearUserDetailsFromContext'],
        on: {
          LOG_IN: {
            target: 'loggedIn',
            actions: 'assignUserDetailsToContext',
          },
        },
      },
    },
  },
  {
    services: {
      checkIfLoggedIn: () => async (
        send: Sender<AuthenticationMachineEvent>,
      ) => {
        // Perform some async check here
        // if (isLoggedIn) {
        //   send({
        //     type: "REPORT_IS_LOGGED_IN",
        //     userDetails: {
        //       username: "mpocock1",
        //     },
        //   });
        // } else {
        //   send({
        //     type: "REPORT_IS_LOGGED_OUT",
        //   });
        // }
      },
    },
    actions: {
      navigateToAuthPage: () => {
        // When the user is logged out, we
        // should take them to the /auth route
      },
      assignUserDetailsToContext: assign((context, event) => {
        if (event.type !== 'REPORT_IS_LOGGED_IN') {
          return {};
        }
        return {
          userDetails: event.userDetails,
        };
      }),
      clearUserDetailsFromContext: assign({
        userDetails: undefined,
      }),
    },
  },
);

export default authenticationMachine;

```

