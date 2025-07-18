
# Stakeholder and Value Modelling Transformations

The following transformations aim at making modelling [stakeholders](/docs/stakeholders/) and [value registers](/docs/value-registers/) more efficient. These language features and transformations shall provide tool-support for applying the [Value-Driven Analysis and Design (VDAD) process](https://ethical-se.github.io/value-driven-analysis-and-design).

## Add Ethical Value Assessment to User Story

As documented under [User Requirements](/docs/user-requirements/) CML provides language features to write user stories and in addition, [Story Valuation according to ESE](https://github.com/ethical-se/ese-practices/blob/main/practices/ESE-StoryValuation.md).

If you have an existing user story in CML that has not been valuated yet, a transformation allows you to generate the additional part:

[![Add Ethical Value Assessment - Example (1)](/img/add-ethical-value-assessment-sample-1.png)](/img/add-ethical-value-assessment-sample-1.png)

This will add the additional part for the story valuation:

[![Add Ethical Value Assessment - Example (2)](/img/add-ethical-value-assessment-sample-2.png)](/img/add-ethical-value-assessment-sample-2.png)

You can then adjust the story with the actual values that are promoted and/or harmed. For example:

[![Add Ethical Value Assessment - Example (3)](/img/add-ethical-value-assessment-sample-3.png)](/img/add-ethical-value-assessment-sample-3.png)

## Create Stakeholder for User Story Role

When applying [Value-Driven Analysis and Design (VDAD)](https://ethical-se.github.io/value-driven-analysis-and-design) or similar approaches, one typically starts with modelling requirements (use cases, user stories, etc.) and then continues with a stakeholder analysis and, later on, elicits ethical values. This transformation allows you to create stakeholders directly from roles inside user stories.

The following example shows such a user story and the transformation you can trigger:

[![Create Stakeholder for User Story Role - Example (1)](/img/create-stakeholder-for-story-role-sample-1.png)](/img/create-stakeholder-for-story-role-sample-1.png)

The transformation will create a `Stakeholders` block with the corresponding stakeholder for your user story role:

[![Create Stakeholder for User Story Role - Example (2)](/img/create-stakeholder-for-story-role-sample-2.png)](/img/create-stakeholder-for-story-role-sample-2.png)

Note that the values for `influence`, `interest` and `description` are just generated default values that you have to adjust manually.

## Create Value for Stakeholder

Once you modelled a stakeholder, you may want to elicit the values that are important for this stakeholder(s). This transformation allows you to automatically generate a CML `Value` construct for a given stakeholder.

The following example shows the transformation offered on stakeholders:

[![Create Value for Stakeholder - Example (1)](/img/create-value-for-stakeholder-sample-1.png)](/img/create-value-for-stakeholder-sample-1.png)

The transformation will create a value register containing a value and the reference to the stakeholder:

[![Create Value for Stakeholder - Example (2)](/img/create-value-for-stakeholder-sample-2.png)](/img/create-value-for-stakeholder-sample-2.png)

**Note** that this transformation generates lots of default values, such as register name, value name, etc., that you have to manually change/define after applying the transformation.

## Create Value Register for Bounded Context

If you already created a domain model and defined a Bounded Context in CML, you might want to generate a [Value Register](/docs/value-registers/) for the specific Bounded Context. This transformation allows you to quickly add a register with the reference to your context.

The following example illustrates the transformation offered on Bounded Contexts:

[![Create Value Register for Bounded Context - Example (1)](/img/create-value-register-for-bounded-context-sample-1.png)](/img/create-value-register-for-bounded-context-sample-1.png)

The transformation creates an empty value register for the context, which can then be filled with the values important to the stakeholders:

[![Create Value Register for Bounded Context - Example (2)](/img/create-value-register-for-bounded-context-sample-2.png)](/img/create-value-register-for-bounded-context-sample-2.png)

## Wrap Value in Cluster

If you have modelled a value inside a value register and now want to use value clusters according to the [IEEE 7000 standard](https://ieeexplore.ieee.org/document/9536679), this transformations allows you to wrap an existing value inside a value cluster.

The following example shows the offered transformation on a value:

[![Wrap Value in Cluster - Example (1)](/img/wrap-value-in-cluster-sample-1.png)](/img/wrap-value-in-cluster-sample-1.png)

The transformation wraps the value accordingly:

[![Wrap Value in Cluster - Example (2)](/img/wrap-value-in-cluster-sample-2.png)](/img/wrap-value-in-cluster-sample-2.png)

Note that you have to adjust the name of the cluster manually after applying the transformation.

**Note:** This transformation (“Wrap Value in Cluster”) has some known technical limitations in Visual Studio Code. We are sorry for that. For the time being, use the Eclipse Plugin if you want to test this transformation.

## Feedback

Please feel free to provide feedback which other transformations would be useful for you. [Get in touch with us](/getting-involved/).

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/modeling-tools/stakeholder-and-value-modelling.md)

---

* [← Previous](/docs/story-splitting/)
* [Next →](/docs/architectural-refactorings/)

