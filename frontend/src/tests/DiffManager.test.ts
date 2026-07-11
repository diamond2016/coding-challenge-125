
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
    mockDefaultApi = vi.fn();
    vi.mocked(DefaultApi).mockImplementation(() => ({
      apiDiffPrettypPost: mockDefaultApi,
    }));
  });

  afterEach(() => {
    mockConsoleError.mockRestore();
  });

  it('should be mounted with initial values', () => {
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
      diff: 'diff result',
    };

    mockDefaultApi.mockResolvedValueOnce(mockResponse);

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

    // Set test values
    wrapper.vm.text1Value = 'test input a';
    wrapper.vm.text2Value = 'test input b';

    // Find and click the Diff button in AppHeader
    const diffButton = wrapper.find('button.diff-button');
    await diffButton.trigger('click');

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
          Text1View: true,
          Text2View: true,
          DiffView: true,
        },
      },
    });

    wrapper.vm.text1Value = 'test input a';
    wrapper.vm.text2Value = 'test input b';

    // Find and click the Diff button in AppHeader
    const diffButton = wrapper.find('button.diff-button');
    await diffButton.trigger('click');

    // Verify error was logged
    await nextTick();
    expect(mockConsoleError).toHaveBeenCalledWith('Error from post diff-prettyp:', mockError);
  });

  it('should update diff value when DiffView emits update:modelValue', async () => {
    const mockDiffValue = 'computed diff result';

    wrapper = mount(DiffManager, {
      global: {
        stubs: {
          AppHeader: true,
          Text1View: true,
          Text2View: true,
          DiffView: {
            template: '<div>{{ modelValue }}</div>',
            props: ['modelValue'],
            emits: ['update:modelValue'],
          },
        },
      },
    });

    // Trigger the update event using Vue Test Utils
    await wrapper.trigger('update:modelValue', mockDiffValue);

    expect(wrapper.vm.textDiffValue).toBe(mockDiffValue);
  });

  it('should handle null value from DiffView', async () => {
    wrapper = mount(DiffManager, {
      global: {
        stubs: {
          AppHeader: true,
          Text1View: true,
          Text2View: true,
          DiffView: {
            template: '<div>{{ modelValue }}</div>',
            props: ['modelValue'],
            emits: ['update:modelValue'],
          },
        },
      },
    });

    // Trigger the update event with null using Vue Test Utils
    await wrapper.trigger('update:modelValue', null);

    expect(wrapper.vm.textDiffValue).toBe('');
  });
});