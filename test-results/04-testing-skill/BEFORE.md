# Test: Testing Patterns Skill - BEFORE

## Test Date
2026-01-15

## Current Configuration
No testing patterns skill defined.

## Test Scenario
User asks for tests for the UserCard component.

## Test File
```typescript
// src/components/UserCard.tsx
interface User {
  id?: string;
  name: string;
  email: string;
  role: 'admin' | 'user';
}

interface UserCardProps {
  user: User;
  onSelect?: (user: User) => void;
}

export function UserCard({ user, onSelect }: UserCardProps) {
  // ... component code
}
```

## Test Prompt
"Write tests for the UserCard component"

## Expected Behavior (Without Skill)
Typical ad-hoc test writing:
- Inconsistent test structure
- Duplicate test data across tests
- Missing edge cases
- Testing implementation rather than behavior

## Simulated Response Without Skill
```typescript
import { render, screen } from '@testing-library/react';
import { UserCard } from './UserCard';

test('renders UserCard', () => {
  const user = { name: 'John', email: 'john@test.com', role: 'user' };
  render(<UserCard user={user} />);
  expect(screen.getByText('John')).toBeInTheDocument();
});

test('shows admin badge', () => {
  const user = { name: 'Jane', email: 'jane@test.com', role: 'admin' };
  render(<UserCard user={user} />);
  expect(screen.getByText('Admin')).toBeInTheDocument();
});

test('calls onSelect', () => {
  const user = { name: 'Bob', email: 'bob@test.com', role: 'user' };
  const onSelect = jest.fn();
  render(<UserCard user={user} onSelect={onSelect} />);
  // ... test code
});
```

## Issues With Ad-Hoc Approach
1. **Duplicate data**: Each test creates its own user object
2. **Inconsistent structure**: No organization by feature/behavior
3. **Missing factory pattern**: No reusable mock creators
4. **Missing edge cases**: No empty state, error handling, etc.
5. **No describe blocks**: Flat test structure

## Risk Assessment
- **Medium Risk**: Inconsistent tests are harder to maintain
- **Issue**: Test files become messy and hard to understand
- **Impact**: Lower test coverage, more bugs reaching production
