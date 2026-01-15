---
name: testing-patterns
description: Jest/Vitest testing patterns, factory functions, mocking strategies, and TDD workflow. Use when writing unit tests, creating test factories, or following TDD red-green-refactor cycle.
---

# Testing Patterns and Utilities

## Testing Philosophy

### Test-Driven Development (TDD)
1. Write failing test FIRST
2. Implement minimal code to pass
3. Refactor after green
4. Never write production code without a failing test

### Behavior-Driven Testing
- Test behavior, not implementation
- Focus on public APIs and business requirements
- Avoid testing implementation details
- Use descriptive test names that describe behavior

### Factory Pattern
- Create `getMockX(overrides?: Partial<X>)` functions
- Provide sensible defaults
- Allow overriding specific properties
- Keep tests DRY and maintainable

## Test Structure Template

```typescript
import { render, screen, fireEvent } from '@testing-library/react';

// Mock dependencies at top
jest.mock('./hooks/useData');

// Factories before tests
const getMockUser = (overrides?: Partial<User>): User => ({
  id: 'user-123',
  name: 'John Doe',
  email: 'john@example.com',
  role: 'user',
  ...overrides,
});

const getMockProps = (overrides?: Partial<ComponentProps>) => ({
  user: getMockUser(),
  onSelect: jest.fn(),
  isLoading: false,
  ...overrides,
});

describe('ComponentName', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('Rendering', () => {
    it('should render with default props', () => {});
    it('should render loading state when loading', () => {});
    it('should render error state on error', () => {});
    it('should render empty state when data is empty', () => {});
  });

  describe('User interactions', () => {
    it('should call onSelect when clicked', async () => {});
    it('should not call onSelect when disabled', () => {});
  });

  describe('Edge cases', () => {
    it('should handle missing optional props', () => {});
    it('should handle very long text', () => {});
  });
});
```

## Factory Pattern Examples

### Props Factory
```typescript
import { ComponentProps } from 'react';

const getMockUserCardProps = (
  overrides?: Partial<ComponentProps<typeof UserCard>>
) => ({
  user: getMockUser(),
  onSelect: jest.fn(),
  isLoading: false,
  ...overrides,
});

// Usage
it('should render with custom title', () => {
  const props = getMockUserCardProps({ isLoading: true });
  render(<UserCard {...props} />);
  expect(screen.getByTestId('loading')).toBeTruthy();
});
```

### Data Factory
```typescript
interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'user';
}

const getMockUser = (overrides?: Partial<User>): User => ({
  id: 'user-123',
  name: 'John Doe',
  email: 'john@example.com',
  role: 'user',
  ...overrides,
});

// Usage - override only what matters for this test
it('should display admin badge for admin users', () => {
  const user = getMockUser({ role: 'admin' });
  render(<UserCard user={user} />);
  expect(screen.getByText('Admin')).toBeTruthy();
});
```

## Mocking Patterns

### Module Mocking
```typescript
// Mock entire module
jest.mock('utils/analytics');

// Mock with implementation
jest.mock('utils/analytics', () => ({
  logEvent: jest.fn(),
  trackPage: jest.fn(),
}));

// Access mock in test
const { logEvent } = jest.requireMock('utils/analytics');
expect(logEvent).toHaveBeenCalledWith('click', { button: 'submit' });
```

### Hook Mocking
```typescript
import { useUser } from './hooks/useUser';

jest.mock('./hooks/useUser');

const mockUseUser = useUser as jest.MockedFunction<typeof useUser>;

// In test setup
mockUseUser.mockReturnValue({
  user: getMockUser(),
  isLoading: false,
  error: null,
});

// For error state
mockUseUser.mockReturnValue({
  user: null,
  isLoading: false,
  error: new Error('Failed to load'),
});
```

## Query Patterns

```typescript
// Element must exist
expect(screen.getByText('Hello')).toBeTruthy();
expect(screen.getByRole('button', { name: 'Submit' })).toBeTruthy();

// Element should NOT exist
expect(screen.queryByText('Goodbye')).toBeNull();

// Element appears asynchronously
await waitFor(() => {
  expect(screen.getByText('Loaded')).toBeTruthy();
});

// Find (returns promise, waits for element)
const button = await screen.findByRole('button', { name: 'Submit' });
```

## User Interaction Patterns

```typescript
import { fireEvent, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

// Click
await userEvent.click(screen.getByRole('button'));

// Type
await userEvent.type(screen.getByLabelText('Email'), 'user@example.com');

// Form submission
it('should submit form with valid data', async () => {
  const user = userEvent.setup();
  const onSubmit = jest.fn();

  render(<LoginForm onSubmit={onSubmit} />);

  await user.type(screen.getByLabelText('Email'), 'test@example.com');
  await user.type(screen.getByLabelText('Password'), 'password123');
  await user.click(screen.getByRole('button', { name: 'Login' }));

  await waitFor(() => {
    expect(onSubmit).toHaveBeenCalledWith({
      email: 'test@example.com',
      password: 'password123',
    });
  });
});
```

## Anti-Patterns to Avoid

### Testing Implementation
```typescript
// Bad - testing internal state
expect(component.state.isOpen).toBe(true);

// Good - testing behavior
expect(screen.getByRole('dialog')).toBeVisible();
```

### Duplicate Test Data
```typescript
// Bad - repeated inline objects
it('test 1', () => {
  const user = { id: '1', name: 'John', email: 'john@test.com', role: 'user' };
});
it('test 2', () => {
  const user = { id: '2', name: 'Jane', email: 'jane@test.com' }; // Missing role!
});

// Good - factory function
const user = getMockUser({ name: 'Custom Name' });
```

### Testing Mock Behavior
```typescript
// Bad - testing that you called the mock
expect(mockFetch).toHaveBeenCalled();

// Good - testing actual outcome
expect(screen.getByText('Data loaded')).toBeTruthy();
```

## Best Practices Checklist

- [ ] Use factory functions for all test data
- [ ] Organize tests with describe blocks
- [ ] Test behavior, not implementation
- [ ] Clear mocks between tests
- [ ] One behavior per test
- [ ] Use meaningful test names
- [ ] Test all UI states (loading, error, empty, success)
- [ ] Test edge cases
- [ ] Avoid snapshot tests for logic
- [ ] Keep tests focused and small
