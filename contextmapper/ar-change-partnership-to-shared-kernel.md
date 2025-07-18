
# AR-11: Change Partnership to Shared Kernel

This simple relationship refactoring changes a Partnership relationship on a Context Map to a Shared Kernel relationship.

## Summary

Our relationship refactorings allow the user/modeller to change the type of a relationship on a Context Map easily without manual work.
The symmetric relationships according to our [semantic model](/docs/language-model/), Shared Kernel and Partnership, are interchangeable without impacts
to the structure of the decomposition. This refactoring changes a Partnership relationship to a Shared Kernel relationship.

**Inverse AR:**

* [AR-10: Change Shared Kernel to Partnership](/docs/ar-change-shared-kernel-to-partnership/)

## Example

The following small example illustrates how this refactoring can be applied. With a right-click on a Partnership relationship, you can apply
*Change to Shared Kernel*:

[![Change Partnership to Shared Kernel Example Input](/img/change-partnership-to-shared-kernel-input.png)](/img/change-partnership-to-shared-kernel-input.png)

The refactoring will simply change the relationship to a Shared Kernel relationship:
[![Change Partnership to Shared Kernel Example Output](/img/change-partnership-to-shared-kernel-output.png)](/img/change-partnership-to-shared-kernel-output.png)

[Improve this page](https://github.com/ContextMapper/contextmapper.github.io/blob/master/_docs/architectural-refactorings/ar-change-partnership-to-shared-kernel.md)

---

* [← Previous](/docs/ar-change-shared-kernel-to-partnership/)
* [Next →](/docs/vdad-support/)

