# Test: Testing Patterns Skill - AFTER

## Test Date
2026-01-15

## New Configuration
Added testing-patterns skill at:
`/Users/maxx/.claude/skills/testing-patterns/SKILL.md`

## Skill Description
```yaml
name: testing-patterns
description: Jest/Vitest testing patterns, factory functions, mocking strategies,
and TDD workflow. Use when writing unit tests, creating test factories, or
following TDD red-green-refactor cycle.
```

## Test Prompt
"Write tests for the UserCard component"

## Expected Behavior (With Skill)

When the skill is loaded, Claude follows structured testing patterns:

### Generated Test File
```typescript
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { UserCard } from './UserCard';

// ============ FACTORIES ============

const getMockUser = (overrides?: Partial<User>): User => ({
  id: 'user-123',
  name: 'John Doe',
  email: 'john@example.com',
  role: 'user',
  ...overrides,
});

const getMockUserCardProps = (
  overrides?: Partial<ComponentProps<typeof UserCard>>
) => ({
  user: getMockUser(),
  onSelect: jest.fn(),
  ...overrides,
});

// ============ TESTS ============

describe('UserCard', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('Rendering', () => {
    it('should render user name and email', () => {
      const props = getMockUserCardProps();
      render(<UserCard {...props} />);

      expect(screen.getByText('John Doe')).toBeTruthy();
      expect(screen.getByText('john@example.com')).toBeTruthy();
    });

    it('should render admin badge for admin users', () => {
      const props = getMockUserCardProps({
        user: getMockUser({ role: 'admin' }),
      });
      render(<UserCard {...props} />);

      expect(screen.getByText('Admin')).toBeTruthy();
    });

    it('should not render admin badge for regular users', () => {
      const props = getMockUserCardProps({
        user: getMockUser({ role: 'user' }),
      });
      render(<UserCard {...props} />);

      expect(screen.queryByText('Admin')).toBeNull();
    });
  });

  describe('User interactions', () => {
    it('should call onSelect when card is clicked', async () => {
      const user = userEvent.setup();
      const onSelect = jest.fn();
      const mockUser = getMockUser();
      const props = getMockUserCardProps({ user: mockUser, onSelect });

      render(<UserCard {...props} />);
      await user.click(screen.getByText('John Doe'));

      expect(onSelect).toHaveBeenCalledTimes(1);
      expect(onSelect).toHaveBeenCalledWith(mockUser);
    });

    it('should not throw when onSelect is not provided', async () => {
      const user = userEvent.setup();
      const props = getMockUserCardProps({ onSelect: undefined });

      render(<UserCard {...props} />);

      await expect(
        user.click(screen.getByText('John Doe'))
      ).resolves.not.toThrow();
    });
  });

  describe('Edge cases', () => {
    it('should handle user with no id', () => {
      const props = getMockUserCardProps({
        user: getMockUser({ id: undefined }),
      });
      render(<UserCard {...props} />);

      expect(screen.getByText('John Doe')).toBeTruthy();
    });

    it('should handle very long names', () => {
      const props = getMockUserCardProps({
        user: getMockUser({ name: 'A'.repeat(100) }),
      });
      render(<UserCard {...props} />);

      expect(screen.getByText('A'.repeat(100))).toBeTruthy();
    });
  });
});
```

## Comparison: Before vs After

| Aspect | Without Skill | With Skill |
|--------|---------------|------------|
| Structure | Flat tests | Organized describe blocks |
| Test data | Inline objects | Factory functions |
| Reusability | Low | High (factories) |
| Edge cases | Often missed | Explicit section |
| Maintenance | Harder | Easier |
| Consistency | Variable | Consistent pattern |

## Key Improvements

### 1. Factory Pattern
```typescript
// Before: Duplicate inline data
const user = { name: 'John', email: 'john@test.com', role: 'user' };

// After: Reusable factory with defaults
const props = getMockUserCardProps({ user: getMockUser({ role: 'admin' }) });
```

### 2. Organized Structure
```
describe('UserCard')
├── describe('Rendering')
│   ├── it('renders user name and email')
│   ├── it('renders admin badge for admin')
│   └── it('does not render admin badge for regular')
├── describe('User interactions')
│   ├── it('calls onSelect when clicked')
│   └── it('handles missing onSelect')
└── describe('Edge cases')
    ├── it('handles missing id')
    └── it('handles long names')
```

### 3. Behavior-Focused Tests
Tests describe what the component DOES, not how it's implemented.

## Impact Assessment

### Benefits
- **Maintainability**: Factory functions reduce duplication
- **Readability**: Organized structure makes tests scannable
- **Coverage**: Explicit edge cases section ensures completeness
- **Onboarding**: Consistent pattern is easier for new developers

### Considerations
- Initial learning curve for factory pattern
- More boilerplate for simple components
- Requires discipline to maintain pattern

## Conclusion
**Recommendation: IMPLEMENT**

This skill provides a consistent testing approach that:
1. Reduces test code duplication
2. Makes tests more maintainable
3. Ensures edge cases are considered
4. Creates readable, self-documenting tests

The upfront investment in factories and structure pays off in long-term maintainability.
