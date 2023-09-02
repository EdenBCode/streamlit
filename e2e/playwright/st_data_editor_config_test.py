# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from playwright.sync_api import Page, expect

from conftest import ImageCompareFunction


def test_data_editor_supports_various_configurations(
    app: Page, assert_snapshot: ImageCompareFunction
):
    """Screenshot test that st.data_editor supports various configuration options."""
    dataframe_elements = app.locator(".stDataFrame")
    expect(dataframe_elements).to_have_count(23)

    # The data editor might require a bit more time for rendering the canvas
    app.wait_for_timeout(250)

    for i, element in enumerate(dataframe_elements.all()):
        assert_snapshot(element, name=f"data_editor-config-{i}")