
# Story Splitting (PoC)

The Context Mapper DSL (CML) supports capturing [user story](/docs/user-requirements/#user-story). Serving as initial input to our [OOAD transformations](/docs/rapid-ooad/), these stories allow our users to start prototyping an application rapidly. Before you start generating Subdomains and Bounded Contexts in such transformations, you have to create and evolve some use cases or user stories. During this process (in case you work with user stories), you may want to [split your stories](https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/). Our story splitting transformations based on [*Patterns for Splitting User Stories*](https://agileforall.com/patterns-for-splitting-user-stories/) support such effort.

**Note:** This feature is in "proof of concept" state. It might not be stable and we currently only support one transformation. In the future we may support more [Patterns for Splitting User Stories](https://agileforall.com/patterns-for-splitting-user-stories/).

## Split Story by Verb/Operation

As a first proof of concept for this feature we implemented the transformation “Split Story by Verb/Operation”. It splits a CML user story by its verb.

We illustrate the idea with the following user story written in CML:

```
UserStory Account_Admin_Story {
    As an "Admin" I want to "manage" an "Account" so that "can enable users to work with the system."
}

```

The Context Mapper editor provides a quick fix on the verb:

[![Story Splitting in VS Code - Example (1)](/img/story-splitting-example-1.png)](/img/story-splitting-example-1.png)

By clicking on the verb and then on the light bulb, users can click “Split Story by Verb/Operation”:

[![Story Splitting in VS Code - Example (2)](/img/story-splitting-example-2.png)](/img/story-splitting-example-2.png)

Users can then enter multiple new verbs, one after the other:

[![Story Splitting in VS Code - Example (3)](/img/story-splitting-example-3.png)](/img/story-splitting-example-3.png)

Once you entered all desired verbs, you can press `ESC` and the transformation will be applied. In our case here we entered the verbs **create**, **edit**, and **cancel**. This leads to the following CML result:

[![Story Splitting in VS Code - Example (4)](/img/story-splitting-example-4.png)](/img/story-splitting-example-4.png)

The resulting CML model is:

```
UserStory Account_Admin_Story split by Account_Admin_Story_Split {
	As an "Admin" I want to "manage" an "Account" so that "can enable users to work with the system."
}

UserStory Account_Admin_Story_Split {
	As an "Admin"
	I want to "cancel" an "Account"
	I want to "edit" an "Account"
	I want to create an "Account"
	so that "can enable users to work with the system."
}

```

With the *split by* keyword we provide a back-reference so that you still know which story was split by which other story (and how the original story looked like).

## Next Steps

After you have modelled and split a sufficient amount user stories, you can use our [OOAD transformations](/docs/rapid-ooad/) to derive Subdomains and Bounded Contexts from them. The transformations will always use the *split* version of a story and ignore the original one!

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/modeling-tools/story-splitting.md)

---

* [← Previous](/docs/rapid-ooad/)
* [Next →](/docs/stakeholder-and-value-modelling-transformations/)

