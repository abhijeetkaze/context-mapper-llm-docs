
# Domain and Subdomain

As bounded contexts, domains are defined on the root level of a CML (\*.cml) file.
They provide a container to specify all subdomains which are then referenced on a bounded context with the *implements* keyword.
A bounded context can also implement the compete domain. Have a look at [bounded context](/docs/bounded-context/) for an example.

## Syntax

The following example illustrates how you can specify a domain with subdomains in CML:

```
/* Syntax example: Domain and Subdomains */
Domain Insurance {
  domainVisionStatement = "Insurance domain vision statement ..."

  Subdomain CustomerManagementDomain {
    type = CORE_DOMAIN
    domainVisionStatement = "Subdomain managing everything customer-related."

    Entity Customer {
      String firstname
      String familyname
    }

    /* Add more entities ... */
  }

  Subdomain ContractManagementDomain {}

  /* Add more subdomains ... */
}

```

Note that the equal sign (=) to assign an attribute value as done in the example above is optional and can be omitted.

### Subdomain Type

With the *type* keyword you specify of which type your subdomain is. The following types exist:

* CORE\_DOMAIN
* SUPPORTING\_DOMAIN
* GENERIC\_SUBDOMAIN

### Implemented Features

The CML language supports the specification of user requirements or features in the form of [use cases or user stories](/docs/user-requirements/).
With the *supports* keyword you can specify which user requirements a Subdomain implements. An example:

```
/* Syntax example for Subdomain that supports specific user requirements: */
Domain Insurance {
  domainVisionStatement = "Insurance domain vision statement ..."

  Subdomain CustomerManagementDomain supports CreateCustomers, CreateCustomerAddresses {
    type = CORE_DOMAIN
    domainVisionStatement = "Subdomain managing everything customer-related."

    Entity Customer {
      String firstname
      String familyname
    }
  }

}

UserStory CreateCustomers {
  As an "Insurance Employee"
    I want to "create" a "Customer" with its "firstname", "lastname"
  so that "I am able to manage the customers data and offer them insurance contracts."
}

UserStory CreateCustomerAddresses {
  As an "Insurance Employee"
    I want to "create" an "Address" for a "Customer"
    I want to "update" an "Address" for a "Customer"
  so that "I am able to manage the customers addresses."
}

```

### Domain Vision Statement

With the *domainVisionStatement* keyword you can specify a vision statement for domains and subdomains, according to the DDD [Domain Vision Statement](/docs/domain-vision-statement/)
pattern.

### Entities

In order to provide further details about your subdomain and which domain objects are part of it, you can use entities within a subdomain. Note that the used *Entity* rule is integrated from the [Sculptor DSL](https://sculptor.github.io/).
For more details about the features and possibilities of this Entity rule, we refer to the [Sculptor documentation](https://sculptor.github.io/documentation/advanced-tutorial).
An example of a simple entity with attributes is illustrated above.

**Note** that only entities can be used within the subdomains. It is not possible to use [Aggregates](/docs/aggregate/) or other
tactic DDD concepts within them. The entities within subdomains are only used for business modeling purposes and not respected by the generator tools. Generators
respect the domain model within Bounded Contexts.

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/language-reference/subdomain.md)

---

* [← Previous](/docs/bounded-context/)
* [Next →](/docs/domain-vision-statement/)

