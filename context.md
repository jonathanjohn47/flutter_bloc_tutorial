# context.md — Flutter BLoC Learning Project Memory

> Persistent memory for Claude teaching sessions. Read this file before any session. Update it whenever the user commits.

---

## Project Status

- **Stage:** Just started. Default `flutter create` counter app still in place.
- **Dependencies installed:** `flutter_bloc: ^9.1.1`, `equatable: ^2.0.8` (added to `pubspec.yaml`, `pub get` run).
- **lib/ contents:** only `lib/main.dart` (default StatefulWidget counter, not yet touched).
- **No BLoC/Cubit code written yet.**

---

## Learning Progress

### Concepts Mastered
- (none yet)

### Concepts Partially Understood
- (none yet)

### Concepts Not Yet Covered
- StatefulWidget → Cubit → Bloc progression
- Events / States
- BlocBuilder / BlocListener / BlocConsumer
- Repository Pattern
- Dependency Injection
- Clean Architecture folder structure
- Hydrated Bloc
- Bloc Testing

**Per CLAUDE.md's Flutter-Specific Learning Order, next concept in queue: StatefulWidget review, then InheritedWidget/Provider context, then Cubit.**

---

## User Misconceptions

- (none observed yet — first session)

---

## Current Exercises

- **In progress:** none
- **Pending:** Convert the default counter app's state management from `setState` to a `CounterCubit` (first exercise, per learning order — Cubit before Bloc).

---

## Important Discoveries / Debugging Insights

- (none yet)

---

## Files Modified (cumulative log)

| Date | File | Change |
|------|------|--------|
| 2026-07-01 | `pubspec.yaml` | Added `flutter_bloc` and `equatable` dependencies |
| 2026-07-01 | `context.md` | Created — initial memory file |

---

## Session Log

### 2026-07-01
- Dependencies installed (`flutter_bloc`, `equatable`).
- `context.md` created to establish learning memory baseline.
- No teaching/implementation has happened yet — next session should start with reviewing the current `setState`-based counter in `lib/main.dart` and asking the user to reason about what problems arise as the widget tree grows, before introducing Cubit.
