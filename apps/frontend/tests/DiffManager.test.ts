import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { mount } from '@vue/test-utils';
import { nextTick } from 'vue';

import DiffManager from '@/views/DiffManager.vue';
import { DefaultApi } from '@/api/client/api';
import type { DiffPrettypRequest, DiffPrettypResponse } from '@/api/client';

// Mock the API client
vi.mock('@/api/client/api', () => ({
  DefaultApi: vi.fn().mockImplementation(() => ({
    apiDiffPost: vi.fn(),
  })),
}));

// Mock console.log to track calls
const mockConsoleLog = vi.spyOn(console, 'log').mockImplementation(() => {});

describe('DiffManager', () => {
  let wrapper: ReturnType<typeof mount<DiffManager>>;
  let mockApiInstance: any;
  let mockApiDiffPost: any;

  beforeEach(() => {
    // Reset all mocks before each test
    vi.clearAllMocks();
    mockConsoleLog.mockClear();

    // Create a mock for DefaultApi
    mockApiInstance = {
      apiDiffPost: vi.fn(),
    };
    vi.mocked(DefaultApi).mockImplementation(() => mockApiInstance);

    // Store reference to the apiDiffPost function
    mockApiDiffPost = mockApiInstance.apiDiffPost;
  });

  afterEach(() => {
    mockConsoleLog.mockRestore();
  });

  it('should be mounted', () => {
    wrapper = mount(DiffManager, {
      global: {
        stubs: {
          AppHeader: true,
        },
      },
    });

    expect(wrapper.exists()).toBe(true);
  });

  it('should have initial values after mount', async () => {
    wrapper = mount(DiffManager, {
      global: {
        stubs: {
          AppHeader: true,
        },
      },
    });

    // Wait for onMounted to set initial values
    await nextTick();
    await nextTick();

    // Check that the component has the expected initial values
    expect(wrapper.vm.text1Value).toBe('Hello World!');
    expect(wrapper.vm.text2Value).toBe('Hello Vue!');
    expect(wrapper.vm.textDiffValue).toBe('');
  });

  it('should call postDiff when Diff button is clicked', async () => {
    const mockRequest: DiffPrettypRequest = {
      string_a: 'test input a',
      string_b: 'test input b',
    };

    const mockResponse: DiffPrettypResponse = {
      data: { diff: 'diff result' },
    };

    // Mock the API call
    mockApiDiffPost.mockResolvedValueOnce(mockResponse);

    wrapper = mount(DiffManager, {
      global: {
        stubs: {
          AppHeader: true, // Keep AppHeader stubbed
        },
      },
    });

    // Set test values directly on refs
    wrapper.vm.text1Value = 'test input a';
    wrapper.vm.text2Value = 'test input b';
    await nextTick();

    // Find the stubbed AppHeader component and trigger its 'diffClick' event
    const appHeaderStub = wrapper.findComponent({ name: 'AppHeader' });
    await appHeaderStub.vm.$emit('diffClick'); // Simulate the click event

    // Verify API was called with correct parameters
    expect(mockApiDiffPost).toHaveBeenCalledWith(mockRequest);

    // Verify response was set
    await nextTick();
    expect(wrapper.vm.textDiffValue).toBe('diff result');
  });

  it('should handle postDiff error gracefully when Diff button is clicked', async () => {
    const mockError = new Error('API Error');
    mockApiDiffPost.mockRejectedValueOnce(mockError);

    wrapper = mount(DiffManager, {
      global: {
        stubs: {
          AppHeader: true, // Keep AppHeader stubbed
        },
      },
    });

    // Set test values directly on refs
    wrapper.vm.text1Value = 'test input a';
    wrapper.vm.text2Value = 'test input b';
    await nextTick();

    // Find the stubbed AppHeader component and trigger its 'diffClick' event
    const appHeaderStub = wrapper.findComponent({ name: 'AppHeader' });
    await appHeaderStub.vm.$emit('diffClick'); // Simulate the click event

    // Verify error was logged (using console.log, not console.error)
    await nextTick();
    expect(mockConsoleLog).toHaveBeenCalledWith('Error in diff-prettyp ', mockError);
  });

  it('should update diff value when DiffView emits update:modelValue', async () => {
    const mockDiffValue = 'computed diff result';

    wrapper = mount(DiffManager, {
      global: {
        stubs: {
          AppHeader: true,
          Text1View: true,
          Text2View: true,
          DiffView: true,
        },
      },
    });

    // Directly set the textDiffValue to simulate receiving update:modelValue
    wrapper.vm.textDiffValue = mockDiffValue;

    expect(wrapper.vm.textDiffValue).toBe(mockDiffValue);
  });

  it('should handle null value from DiffView', async () => {
    wrapper = mount(DiffManager, {
      global: {
        stubs: {
          AppHeader: true,
        },
      },
    });

    // Find the DiffView component by selector and trigger the update event on it with null
    const diffView = wrapper.find('.diff-container');
    await diffView.trigger('update:modelValue', '');

    expect(wrapper.vm.textDiffValue).toBe('');
  });
});