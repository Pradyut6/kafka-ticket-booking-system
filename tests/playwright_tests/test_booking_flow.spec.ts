import { test, expect } from '@playwright/test';

test('Booking API endpoint should respond', async ({ request }) => {
  const response = await request.post('http://localhost:8000/book', {
    data: {
      user_id: 1,
      event_id: 100,
      seat_number: "A12"
    }
  });
  expect(response.ok()).toBeTruthy();
});

