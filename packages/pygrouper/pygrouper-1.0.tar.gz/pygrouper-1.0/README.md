# description

### goal
    
the project aims to provide simple to use events cross-referencing engine

### cases of usage
suppose you have users in database and you want to collect information on their visits to some pages; you use a third-party organisation for this end; you construct an API to accept visit events from your partner; this third-party partner knows nothing (and he should not) about your users database ID; in case of someone visiting page this partner marks him with cookie and sends event to your API containing cookie as an identificator;

here comes the problem of `matching third-party identificators with your internal ones`; 

### assumptions
**users table in your database has columns with third party identificators**
* for this to hold you should have some internal events (like registration) which can enrich user profiles with third-party identificator
___
#### basic case
you have a set of events from third party along with events for grouping (which has database ID) from your database  

let's look at basic case where user registered at your service and visited some pages; registration event provided the same cookie which third party used for this used identification; we have the following events incoming to the algorithm
 
**db_id**|**cookie**|**event_id**
:---:|:---:|:---:
123| "nice_page_visitor"| --
--|"nice_page_visitor"|1
--|"nice_page_visitor"|2

this incoming configuration will produce the following result (pseudocode)

```python
{db_id: { 
    123: {
        cookie: {
            "nice_page_visitor":[
                event1,
                event2,
            ]
        }
    }
}}
```

we successfully matched events from third-party with our internal identificator therefore enriched our users profile; 
___

# python version
\>=3.6

# logging
this package has default logging that uses configuration you provided in your application; for more info see this  [extract](https://docs.python.org/3/howto/logging.html#logging-from-multiple-modules) from official logging doc

# contribution
feel free to PR or create issues