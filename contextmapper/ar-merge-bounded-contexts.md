
# AR-7: Merge Bounded Contexts

Merges two bounded contexts together. The result is one bounded context containing all the aggregates of the two input bounded
contexts.

**Known limitation:** Unfortunately, this AR does not work in [VS Code](/docs/vs-code/) and [online](/docs/online-ide/) in case the removed Bounded Context is referenced in a Context Map. This is due to [a bug in the Xtext framework](https://github.com/eclipse/xtext-core/issues/1494).

## Context & Rationales

By decomposing a system into multiple bounded contexts we aim for loose coupling between the bounded context and a high cohesion
within them. However, sometimes a decomposition may be too fine-granular and merging bounded contexts with a high
coupling together improves the cohesion within the corresponding resulting bounded context.

## Goal

This Architectural Refactoring (AR) merges two bounded contexts together. The resulting bounded context contains all aggregates
of the two input bounded contexts. It can be applied if two bounded context are tightly coupled and the aggregates somehow
belong together. This may improve the cohesion within the resulting bounded context.

**Notes:**

* By applying this AR multiple times you may end with one single Bounded Context and an empty Context Map (no relationships).
* The AR merges all Bounded Context attributes (such as *exposed aggregates*, *implementation technology*, etc.) which are possible
  to merge. However, there are still attributes which cannot be merged (such as the *name* or the *domain vision statement*).
  + All attributes which cannot be merged are taken from the first Bounded Context (by default) selected in the dialog
    (see screenshot below).
  + You have to use the corresponding checkbox on the input dialog, if you want to take the attributes from the second Bounded Context.

**Inverse AR’s:**

* [AR-4: Extract Aggregates by Volatility](/docs/ar-extract-aggregates-by-volatility/)
* [AR-5: Extract Aggregates by Cohesion](/docs/ar-extract-aggregates-by-cohesion/)
* [AR-2: Split Bounded Context by Use Cases](/docs/ar-split-bounded-context-by-use-cases/) (may need multiple merges to completely revert)
* [AR-3: Split Bounded Context by Owner](/docs/ar-split-bounded-context-by-owners/) (may need multiple merges to completely revert)

## Preconditions

* Your model needs **at least two bounded contexts** to merge.

## Input

* Two bounded contexts.

## Output

* One bounded context containing all aggregates of the two input bounded contexts.

## Example

The following example illustrates how this AR can be applied. The corresponding sources can be found in our
[examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings).

### Input

The following model contains two bounded contexts with one aggregate each. Therefore the AR is available on both bounded contexts:

[![Merge Bounded Contexts Example Input](/img/merge-bounded-contexts-input.png)](/img/merge-bounded-contexts-input.png)

### Selection Dialog

After triggering this refactoring, a dialog pops up on which you can choose with which other bounded context you want to merge:

[![Merge Bounded Contexts Example Dialog](/img/merge-bounded-contexts-dialog.png)](/img/merge-bounded-contexts-dialog.png)

**Note:** Use the checkbox "Take attributes which cannot be merged (incl. Bounded Context name) from second Bounded
Context.", if you prefer that the attributes which cannot be merged (also see hint [above](#goal)) are taken from the
second Bounded Context. **By default, the attributes are taken from the first Bounded Context.**

### Result

The resulting model contains one bounded context with both aggregates of the selected bounded contexts:

[![Merge Bounded Contexts Example Output](/img/merge-bounded-contexts-output.png)](/img/merge-bounded-contexts-output.png)

## Example Sources

* You can find the CML sources for this AR example
  [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings/AR-7-Merge-Bounded-Contexts).

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/architectural-refactorings/ar-merge-bounded-contexts.md)

---

* [← Previous](/docs/ar-merge-aggregates/)
* [Next →](/docs/ar-extract-shared-kernel/)

