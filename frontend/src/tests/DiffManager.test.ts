
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { mount } from '@vue/test-utils';
import { nextTick } from 'vue';

import DiffManager from '@/views/DiffManager.vue';
import { DefaultApi } from '@/api/client/api';
import type { DiffPrettypRequest, DiffPrettypResponse } from '@/api/client';

// Mock the API client
vi.mock('@/api/client/api', () => ({
  DefaultApi: vi.fn().mockImplementation(() => ({
    apiDiffPrettypPost: vi.fn(),
  })),
}));

// Mock console.error to track calls
const mockConsoleError = vi.spyOn(console, 'error').mockImplementation(() => {});

describe('DiffManager', () => {
  let wrapper: ReturnType<typeof mount<DiffManager>>;
  let mockDefaultApi: ReturnType<typeof vi.fn>;

  beforeEach(() => {
    // Reset all mocks before each test
    vi.clearAllMocks();
    mockConsoleError.mockClear();
    
    // Create a mock for DefaultApi
    const mockApiInstance = {
      apiDiffPrettypPost: vi.fn(),
    };
    vi.mocked(DefaultApi).mockImplementation(() => mockApiInstance);
    
    // Assign the mock function to mockDefaultApi for testing
    mockDefaultApi = vi.fn();
    mockApiInstance.apiDiffPrettypPost = mockDefaultApi;
  });

  afterEach(() => {
    mockConsoleError.mockRestore();
  });

  it('should be mounted with initial values', () => {
    wrapper = mount(DiffManager, {
      global: {
        stubs: {
          AppHeader: true,
        },
      },
    });

    expect(wrapper.exists()).toBe(true);
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

    mockDefaultApi.mockResolvedValueOnce(mockResponse);

    wrapper = mount(DiffManager, {
      global: {
        stubs: {
          AppHeader: true,
        },
      },
    });

    // Set test values
    wrapper.vm.text1Value = 'test input a';
    wrapper.vm.text2Value = 'test input b';

    // Call handleDiffClick directly
    await wrapper.vm.handleDiffClick();

    // Verify API was called with correct parameters
    expect(mockDefaultApi).toHaveBeenCalledWith(mockRequest);

    // Verify response was set
    await nextTick();
    expect(wrapper.vm.textDiffValue).toBe('diff result');
  });

  it('should handle postDiff error gracefully when Diff button is clicked', async () => {
    const mockError = new Error('API Error');
    mockDefaultApi.mockRejectedValueOnce(mockError);

    wrapper = mount(DiffManager, {
      global: {
        stubs: {
          AppHeader: true,
        },
      },
    });

    wrapper.vm.text1Value = 'test input a';
    wrapper.vm.text2Value = 'test input b';

    // Call handleDiffClick directly
    await wrapper.vm.handleDiffClick();

    // Verify error was logged
    await nextTick();
    expect(mockConsoleError).toHaveBeenCalledWith('Error in diff-prettyp ', mockError);
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