# context.md — Flutter BLoC Learning Project Memory

> Persistent memory for Claude teaching sessions. Read this file before any session. Update it whenever the user commits.

---

## Project Status

- **Stage:** Default `flutter create` counter app still in `lib/main.dart` (not yet wired to Bloc). First Cubit written and compiling.
- **Dependencies installed:** `flutter_bloc: ^9.1.1`, `equatable: ^2.0.8` (added to `pubspec.yaml`, `pub get` run).
- **Folder structure decided:** feature-first Clean Architecture (`lib/features/<feature>/presentation|domain|data/...` + `lib/core/`). User declined a deep-dive into the reasoning for each layer and accepted the structure as given — do not re-litigate this unless user asks.
- **lib/ contents:** `lib/main.dart` (default StatefulWidget counter, not yet touched) + new `lib/features/counter/presentation/bloc/counter_cubit.dart` containing a working `CounterCubit`.
- **`CounterCubit` written and compiling** (see Session 3). Not yet wired into `main.dart`.

---

## Learning Progress

### Concepts Mastered
- **Prop drilling problem:** understands that passing state through constructors across screens forces every intermediate widget to forward data it doesn't care about, coupling unrelated widgets.
- **Why business logic shouldn't live in a widget's State class:** correctly reasoned (after simplification, without testing framing) that counting logic tied to `_MyHomePageState` only exists because that widget exists — pulling it into a standalone class lets multiple screens share it without duplication.
- **Cubit notification model (conceptual):** correctly identified, in his own words, that a Cubit runs a stream and widgets subscribe to it; the Cubit — not the widget — decides when a rebuild-triggering value is emitted. This is the core mental shift from `setState` (widget-initiated) to Cubit (state-holder-initiated).
- **Cubit constructor / initial state:** wrote `CounterCubit() : super(0)` correctly on the first try — understands that `Cubit`'s own constructor requires an initial state to be passed up via `super(...)`.
- **Debugging an unresolved-symbol error:** given the analyzer message "Classes can only extend other classes" (with an offer to auto-generate a blank `Cubit` class), user correctly diagnosed — once prompted to check — that this meant `Cubit` wasn't recognized, i.e. missing `import 'package:flutter_bloc/flutter_bloc.dart';`. Reinforce this pattern later: "IDE offers to create a class with the name you used" is a strong signal of an unresolved import, not a real type error.

### Concepts Partially Understood
- **InheritedWidget / Provider:** given a plain-language explanation (state placed in an ancestor, descendants pull it via `BuildContext` lookup instead of props being pushed down) and told this is what `BlocProvider` / `context.read<T>()` will later use. Not yet reinforced with hands-on use — revisit briefly when `BlocProvider` is introduced.
- **GetX comparison:** user has prior GetX experience (global reactive controllers/service locator). Flagged as a useful reference point for later contrasting GetX's approach vs. Bloc's approach — has not yet been discussed in depth.

- **Why `emit()` instead of direct state mutation:** asked twice (once right after the exercise was assigned, once after the code compiled) — **user has not yet answered this**. Do not assume understanding here; re-ask explicitly at the start of next session before moving on to `BlocProvider`/`BlocBuilder`.

### Concepts Not Yet Covered
- Cubit syntax/API specifics (`extends Cubit<int>`, `emit()`, constructor `super(0)`)
- BlocBuilder / BlocListener / BlocConsumer
- Bloc (vs Cubit) and Events/States
- Repository Pattern
- Dependency Injection
- Clean Architecture folder structure
- Hydrated Bloc
- Bloc Testing (explicitly deferred — user has zero testing background, see misconceptions/notes below)

**Per CLAUDE.md's Flutter-Specific Learning Order, current position: StatefulWidget reviewed → InheritedWidget/Provider introduced conceptually → now entering Cubit.**

---

## User Misconceptions

- None architectural. Note: user initially assumed constructor-passing was the only option for cross-screen state sharing, which is correct as a baseline but was used as the entry point to reveal prop-drilling pain — not a misconception, just the expected starting point.

---

## Teaching Notes / User Preferences (important for future sessions)

- **No testing background at all.** Explaining concepts via "how would you test this" analogies did NOT land and confused the user. Avoid testing-based framing for explaining *other* concepts (e.g., don't use "testability" as the reason to separate logic from widgets). When Bloc Testing is eventually reached (learning order step 15), it will need to be introduced from first principles, assuming zero prior exposure.
- User responds well to concrete "imagine this scenario" framing (e.g., second screen needing the same counter) once abstract/generic questions are simplified.
- User can get discouraged by multi-part or abstract questions ("your questions are too tough") — prefer single, concrete, scenario-based questions one at a time over stacked/compound questions.

---

## Current Exercises

- **Completed:** `CounterCubit` exercise (extends `Cubit<int>`, constructor with initial state `0`, `increment()` emitting `state + 1`) — written by the user at `lib/features/counter/presentation/bloc/counter_cubit.dart`, debugged (missing import), now compiling cleanly.
- **Next up:** Before moving to `BlocProvider`/`BlocBuilder`, re-ask the still-unanswered "why `emit()` instead of direct state mutation" question. Then wire `CounterCubit` into `main.dart` using `BlocProvider` and `BlocBuilder`, replacing `setState`. Then eventually progress to Bloc (Events/States) per learning order.

---

## Important Discoveries / Debugging Insights

- **"Classes can only extend other classes" + IDE offering "Create class 'X'"** is the analyzer's way of saying the superclass name is unresolved — almost always a missing import, not a genuine type-hierarchy problem. Worth reusing as a general debugging heuristic later.

---

## Files Modified (cumulative log)

| Date | File | Change |
|------|------|--------|
| 2026-07-01 | `pubspec.yaml` | Added `flutter_bloc` and `equatable` dependencies |
| 2026-07-01 | `context.md` | Created — initial memory file |
| 2026-07-01 | `context.md` | Updated after teaching session covering prop drilling, InheritedWidget/Provider (conceptual), separation of business logic, and Cubit's stream-based notification model |
| 2026-07-01 | `lib/features/counter/presentation/bloc/counter_cubit.dart` | Created by user: `CounterCubit extends Cubit<int>` with `super(0)` constructor and `increment()` emitting `state + 1`. Fixed missing `flutter_bloc` import that caused an unresolved-superclass error. |
| 2026-07-01 | `context.md` | Updated after Session 3 (folder structure decision, CounterCubit exercise completed + debugged) |

---

## Session Log

### 2026-07-01 (Session 1)
- Dependencies installed (`flutter_bloc`, `equatable`).
- `context.md` created to establish learning memory baseline.

### 2026-07-01 (Session 2)
- Reviewed the default `setState`-based counter in `lib/main.dart` with the user.
- Walked through prop drilling by having the user reason through a cross-screen state-sharing scenario; user correctly identified the problem themselves.
- Introduced InheritedWidget/Provider conceptually (ancestor-holds-state, descendants-pull-via-context) as the mechanism `BlocProvider` later relies on — not yet exercised hands-on.
- Discussed why business logic (the "add 1" rule) shouldn't live inside a widget's `State` class. Initial framing used testing as the motivating example — this did NOT work, user has no testing background and got confused/discouraged. Reframed successfully using a "second screen needs the same logic" scenario instead. **Lesson for future sessions: avoid testing analogies with this user until Bloc Testing is explicitly reached.**
- Introduced the concept of a Cubit as a plain, screen-independent class holding state, and its stream-based notification model (Cubit emits, widgets subscribe) as the replacement for `setState`. User correctly explained this back in their own words.
- Assigned exercise: write a `CounterCubit` (extends `Cubit<int>`, initial state 0, `increment()` emitting `state + 1`). User has not yet attempted/submitted this — pick up here next session.

### 2026-07-01 (Session 3)
- User asked to see the "industry standard" Bloc folder structure before writing any code. Given the feature-first Clean Architecture layout (`features/<name>/presentation|domain|data`, `core/`) as a reference. User explicitly declined the anatomy/reasoning discussion for it ("I don't want to do the anatomy of folder structures... I will accept it as it is") — accepted the structure at face value. **Do not force this discussion again unless user brings it up.**
- User wrote `CounterCubit` themselves at `lib/features/counter/presentation/bloc/counter_cubit.dart`: `extends Cubit<int>`, `CounterCubit() : super(0)`, `increment()` calling `emit(state + 1)` — correct on the substance the first time.
- Hit a real compile error: analyzer said "Classes can only extend other classes" and offered to auto-generate a class named `Cubit`. Walked user through debugging via the actual error message rather than guessing; user correctly diagnosed (once prompted to check) that the `flutter_bloc` import was missing. Added `import 'package:flutter_bloc/flutter_bloc.dart';` and the error cleared.
- Asked (twice) why `emit()` is used instead of directly mutating `state` — **user has not answered this yet**, conversation moved to debugging instead. Must re-ask before proceeding to `BlocProvider`/`BlocBuilder`.
- Session ended here at user's request ("that's for today"). Changes committed to git.
