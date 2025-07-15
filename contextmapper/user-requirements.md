
# User Requirements

As described in our [Rapid Object-oriented Analysis and Design](/docs/rapid-ooad/) page, the CML syntax supports the specification of user stories and use cases.
One can then derive DDD Subdomains and later Bounded Contexts from these stories and cases.

The following examples illustrate the syntax for both concepts quickly. Both concepts allow to specify the *actor*/*user*, the *interactions* (*so that I can* part of user story),
and the *benefit* of a use case or user story.

## Use Case

The syntax to declare a use case rather briefly is as follows:

```
UseCase UC1_Example {
  actor = "Insurance Employee"
  interactions = create a "Customer", update a "Customer", "offer" a "Contract"
  benefit = "I am able to manage the customers data and offer them insurance contracts."
}

```

The predicate (verb) in the `interaction` can be one of the keywords `create`, `read`, `update`, `delete` (CRUD), or any string.

Optionally, it is further possible to add *attributes* to the Entities and/or a reference to another Entity that acts as a *container*. The following example illustrates
the use case including this features:

```
UseCase UC1_Example {
  actor "Insurance Employee"
  interactions
    create a "Customer" with its "firstname", "lastname",
    update an "Address" for a "Customer",
    "offer" a "Contract" for a "Customer"
  benefit "I am able to manage the customers data and offer them insurance contracts."
}

```

The entity attributes follow the keyword *with its* as illustrated above. The reference to the container Entity can be modelled with the following keywords: *for a*,
*for an*, *in a*, *in an*.

### Cockburn Styles

Our grammar supports creating Use Cases according to the *brief* or *casual* format [suggested by A. Cockburn](https://en.wikipedia.org/wiki/Use_case#Cockburn_style),
but gives the prose paragraphs some structure. The following example illustrates the Use Case 2 (“Get paid for car accident”) of [A. Cockburn’s book](https://www.amazon.de/Writing-Effective-Crystal-Software-Development/dp/0201702258)
written in CML:

```
UseCase Get_paid_for_car_accident { // title
  actor "Claimant" // primary actor
  scope "Insurance company" // scope
  level "Summary" // level
  benefit "A claimant submits a claim and and gets paid from the insurance company." // story (brief summary)
}

```

We do not support all attributes for a *fully dressed* Use Case (another style [suggested by A. Cockburn](https://en.wikipedia.org/wiki/Use_case#Cockburn_style)), but
you can use the *interactions* introduced above to model the *main success scenario*:

```
UseCase Get_paid_for_car_accident { // title
  actor "Claimant" // primary actor
  scope "Insurance company" // scope
  level "Summary" // level
  benefit "A claimant submits a claim and and gets paid from the insurance company." // story (brief summary)
  interactions
    "submit" a "Claim",                // step 1: claimant submits claim
    "verifyExistanceOf" "Policy",      // step 2: insurance company verifies that valid policy exists
    "assign" an "Agent" for a "Claim", // step 3: agent is assigned to claim
    "verify" "Policy",                 // step 4: agent verifies all details are within policy guidelines
    "pay" "Claimant",                  // step 5 (1): claimant gets paid
    "close" "Claim"                    // step 5 (2): file/claim gets closed
}

```

### Secondary Actors

If your use case involves secondary actors, you can use the *secondaryActors* keyword as shown in the following example:

```
UseCase UC1_Example {
  actor = "Insurance Employee"
  secondaryActors = "Insurance Administrator", "Sales Person"
  interactions = create a "Customer", update a "Customer", "offer" a "Contract"
  benefit = "I am able to manage the customers data and offer them insurance contracts."
}

```

All actors are respected in our [PlantUML Generator (Use Case Diagram)](/docs/plant-uml/).

## User Story

First and foremost, a user story is an invitation to communicate and collaborate, as well a planning item. That said, the [role-feature-reason template](https://www.agilealliance.org/glossary/user-story-template/) can also serve as a requirements specification element. Hence, the user story support in CML allows you to declare exactly the same information as seen in the use case above, but in another syntax:

```
UserStory US1_Example {
  As an "Insurance Employee"
    I want to "create" a "Customer" with its "firstname", "lastname" // attributes are optional ('with its' part)
    I want to "update" an "Address" for a "Customer" // reference is optional ('for a' part)
    I want to "offer" a "Contract" for a "Customer" // reference is optional ('for a' part)
  so that "I am able to manage the customers data and offer them insurance contracts."
}

```

*Note:* As you can see above, both variants allow users to specify multiple *interactions* or *I want to* parts in one use case or user story. You can see this as a way of
expressing related features, for instance those originating from splitting a larger story - or the steps in a use case scenario.

### Story Valuation

Since Context Mapper version 6.12.x, the user story syntax supports [story valuation](https://github.com/ethical-se/ese-practices/blob/main/practices/ESE-StoryValuation.md). A user story with the existing `As a`, `I want to` and `so that` parts can now be enhanced with promoted and harmed [ethical values](https://github.com/ethical-se/ese-practices/blob/v11/ESE-Glossary.md#ethical-value), as shown in the following example:

```
UserStory SampleStory {
  As a "prospective customer of Lakeside Mutual" // a fictitious insurance company
  I want to "manage" the "PersonalDataProfile"
  so that "I am offered a valid and fair insurance rate"
  and that "data privacy" is promoted
  accepting that "accountability and auditability" are harmed
}

```

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/language-reference/user-requirements.md)

---

* [← Previous](/docs/application-and-process-layer/)
* [Next →](/docs/stakeholders/)

