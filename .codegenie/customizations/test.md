# Testing Practices Cheat Sheet

## Testing Libraries and Frameworks

- Jest: Primary testing framework
- Enzyme: For React component testing
- @testing-library/react: For React component testing
- Sinon: For mocking and stubbing
- Chai: Assertion library

## Mocking and Stubbing

### Jest Mocks

```javascript
jest.mock('module-name');
jest.spyOn(object, 'method').mockImplementation(() => mockReturnValue);
```

### Sinon Stubs

```javascript
const stub = sinon.stub(object, 'method').returns(mockValue);
```

## Fake Implementations

### In-Memory Databases

```javascript
const fakeDb = {
  users: [],
  addUser: (user) => fakeDb.users.push(user),
  getUser: (id) => fakeDb.users.find(u => u.id === id)
};
```

### Mock API Responses

```javascript
const mockApiResponse = {
  data: [
    { id: 1, name: 'Item 1' },
    { id: 2, name: 'Item 2' }
  ]
};
```

## Test Structure

### Describe-It Pattern

```javascript
describe('ComponentName', () => {
  it('should render correctly', () => {
    // Test implementation
  });
});
```

### Given-When-Then Pattern

```javascript
describe('Given a user is logged in', () => {
  beforeEach(() => {
    // Setup logged-in state
  });

  it('When they visit the profile page, Then their information should be displayed', () => {
    // Test implementation
  });
});
```

## Assertion Styles

### Jest Expect

```javascript
expect(result).toBe(expectedValue);
expect(array).toContain(item);
```

### Chai Assertions

```javascript
expect(result).to.equal(expectedValue);
expect(array).to.include(item);
```

## Component Testing

### Shallow Rendering

```javascript
const wrapper = shallow(<Component props={mockProps} />);
```

### Full DOM Rendering

```javascript
const { getByTestId } = render(<Component props={mockProps} />);
```

## Async Testing

### Async/Await

```javascript
it('should fetch data asynchronously', async () => {
  const result = await fetchData();
  expect(result).toEqual(expectedData);
});
```

### Promise Resolving

```javascript
it('should resolve promise', () => {
  return expectPromise.resolves.toBe(expectedValue);
});
```

## Test Coverage

- Use Jest's built-in coverage reporter
- Aim for high coverage, especially in critical paths

## Best Practices

1. Use descriptive test names
2. Keep tests isolated and independent
3. Use setup and teardown functions (beforeEach, afterEach)
4. Mock external dependencies
5. Test both positive and negative scenarios
6. Use snapshot testing for UI components sparingly
7. Prefer integration tests over excessive unit tests for complex interactions

## Custom Test Utilities

- Create helper functions for common test setup tasks
- Use custom matchers for domain-specific assertions

## Continuous Integration

- Run tests automatically on each pull request
- Enforce passing tests before merging